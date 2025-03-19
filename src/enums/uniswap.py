from enum import Enum


class UniswapFee(Enum):
    FEE_100 = 100       # 0.01% - Best for stablecoin pairs (e.g., USDC/DAI)
    FEE_500 = 500       # 0.05% - Blue-chip assets with low volatility (e.g., ETH/USDC)
    FEE_1000 = 1000     # 0.1%  - Mid-volatility pairs (e.g., ETH/DAI, WBTC/ETH)
    FEE_3000 = 3000     # 0.3%  - High-volatility pairs (e.g., ETH/ALT, WBTC/DAI)
    FEE_10000 = 10000   # 1%    - Exotic, low-liquidity pairs (e.g., SHIB/new tokens)
