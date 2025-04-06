
# Get the price of the asset

# p_fair: Price quoted by the Oyster (SynFutures) AMM by combining all the concentrated liquidity and limit orders,
# like the mid-price of a CLOB system.

SECONDS_DAY = 86400


def estimate_profit(position_size: int, p_fair: int, p_spot: int, time_seconds=60):
    return position_size * ((p_fair - p_spot) / p_spot) * (time_seconds / SECONDS_DAY)
