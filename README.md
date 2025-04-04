# perp-arb

Funding rate arbitrage project

## Overview

Perpetual futures platforms typically use funding rates keep the price of the future closely aligned with the true (oracle) price.

If the price of the perpetual future is 5% higher than the oracle price then the platform will incentivise users to go
short to keep the price in check (and vice versa if the perpetual future price is lower than the oracle price). 
This leads to an intentional funding rate arbitrage opportunity.

## Strategy

1. Identify the SynFutures perpetual future price `F_p`
2. Identify the oracle price of the pair (initially using a liquid DEX price as a proxy for this) `O_p`
3. Obtain the signal strength `F_p / O_p` (which must be greater than some value to justify arbitrage)
4. Purchase the asset, and add it to the perpetual futures platform so that it can be used for trading.
5. Go short on the perptual future with 1x leverage so that the trade is delta neutral. The margin used will be the same as the short size.
6. Exit when `F_p <= O_p`.
7. Remove the margin (and potential profit) from the perpetual futures platform and swap this back to some low risk asset e.g., USDC.

Initially this will only consider going short on the perpetual future for the ease of keeping the trade delta neutral (with spot margin acting as a hedge)

## Tax Implications
Having a highly volatile asset as margin is less than ideal because any price increases will incur capital gains that get
cancelled out by the short position. Ideally the margin would be relatively stable. This means there is capital gains risk,
in addition to the tax which would be paid on funding rate earnings (classified as income tax).

