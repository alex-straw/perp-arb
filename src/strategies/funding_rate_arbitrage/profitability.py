def funding_rate_per_window(
        p_fair: float,
        p_spot: float,
        oi_long: int,
        oi_short: int,
        dt: int,
        interval: int = 3_600,
) -> tuple[float, float]:
    """
    Incremental funding‑rate update for a SynFutures perpetual pair.

    Parameters
    ----------
    p_fair : float
        AMM mid‑price of the perpetual (post‑trade tick).
    p_spot : float
        Oracle‑smoothed index price of the underlying, fetched via the
        SynFuturesObserver (the value itself lives inside the Instrument
        contract).
    oi_long : int
        Long open‑interest (trader positions only, LPs excluded).
    oi_short : int
        Short open‑interest.
    dt : int
        Seconds elapsed since the AMM’s funding index last moved.
        **Clamp to `interval` upstream** – stale pools shouldn’t accrue
        more than one funding cycle in a single jump. (very inactive pairs)
    interval : int, default ``3_600`` (1h)
        Funding cycle configured on‑chain (1h, 8h, or 24h).

    Returns
    -------
    (rate_long, rate_short) : tuple[float, float]
        *Positive*→ that side **receives** funding.
        *Negative*→ that side **pays** funding.
        Cash‑flow always nets to zero:
        ``rate_long×oi_long  +  rate_short×oi_short  ==  0``.

    Mechanics
    ---------
    gap           = (p_fair − p_spot) / p_spot
    prorata_rate  = gap × dt / interval

    * **Who pays?**
      + gap>0 ⇒ longs pay, shorts receive
      + gap<0 ⇒ shorts pay, longs receive
    * **Imbalance damping** – the *paying* side is charged the full
      rate; the *receiving* side is scaled by the OI ratio to keep the
      pool cash‑neutral and to reward traders who take the thin side.

    Strategy context
    ----------------
    + Short‑perp / long‑spot when gap>0 and longs dominate; funding
      carry plus basis convergence pays you.
    + Short trade pushes `p_fair` lower **and** raises `oi_short`,
      shrinking the gap and reducing the damping – a self‑balancing
      incentive.
    """

    dt = min(dt, interval)  # One update can never accrue more than one funding cycle.

    # No counter‑party therefore no funding
    if oi_long == 0 or oi_short == 0:
        return 0.0, 0.0

    gap = (p_fair - p_spot) / p_spot            # >0 then longs should pay
    r = gap * dt / interval                     # base rate, un‑dampened

    if gap >= 0:
        rate_long = -r                          # longs pay full rate
        rate_short = r * oi_long / oi_short     # shorts receive, dampened
    else:
        rate_long = r * oi_short / oi_long      # longs receive, dampened
        rate_short = -r                         # shorts pay full rate

    return rate_long, rate_short
