from src.enums.enum_definitions import Network, Contract


ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

ERC20_DECIMALS = {
    Contract.WETH: 18,
    Contract.USDC: 6,
    Contract.ALB: 18
}


CONTRACT_ADDRESSES = {
    Contract.UniswapV3Factory: {
        Network.SEPOLIA: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        Network.ETHEREUM: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        Network.ARBITRUM: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        Network.OPTIMISM: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        Network.BASE: "0x33128a8fC17869897dcE68Ed026d694621f6FDfD"
    },
    Contract.AlienBaseUniswapV3Factory: {
        Network.BASE: "0x0Fd83557b2be93617c9C1C1B6fd549401C74558C"
    },
    Contract.UniswapV3SwapRouter: {
        Network.SEPOLIA: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        Network.ETHEREUM: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        Network.ARBITRUM: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        Network.OPTIMISM: "0xE592427A0AEce92De3Edee1F18E0157C05861564"
    },
    Contract.SynFuturesGate: {
        Network.BASE: "0x208B443983D8BcC8578e9D86Db23FbA547071270",
        Network.BLAST: "0x6A372dBc1968f4a07cf2ce352f410962A972c257"
    },
    Contract.SynFuturesConfig: {
        Network.BASE: "0xB63902d38738e353f3f52AdD203C418A0bFEa172",
    },
    Contract.SynFuturesGuardian: {
        Network.BASE: "0xBe0F37274AdADb32441acDB74791de159B0BD87E",
    },
    Contract.SynFuturesObserver: {
        Network.BASE: "0xDb166a6E454d2a273Cd50CCD6420703564B2a830",
    },
    Contract.SynFuturesInstrumentALBUSDC: {
        Network.BASE: "0xb146f1e409d45862354bebc3acdfb31e0e1488dc"
    },
    Contract.WETH: {
        Network.SEPOLIA: "0x7b79995e5f793A07Bc00c21412e50Ecae098E7f9",
        Network.ETHEREUM: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        Network.ARBITRUM: "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        Network.OPTIMISM: "0x4200000000000000000000000000000000000006",
        Network.BASE: "0x4200000000000000000000000000000000000006"
    },
    Contract.USDC: {
        Network.ETHEREUM: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        Network.ARBITRUM: "0xFF970A61A04b1cA14834A43f5de4533eBDDB5CC8",
        Network.OPTIMISM: "0x7F5c764cBc14f9669B88837ca1490cCa17c31607",
        Network.BASE: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
    },
    Contract.ALB: {
        Network.BASE: "0x1dd2d631c92b1aCdFCDd51A0F7145A50130050C4"
    }
}


INFURA_NETWORKS = {
    Network.SEPOLIA: "https://sepolia.infura.io/v3/",
    Network.ARBITRUM: "https://arbitrum-mainnet.infura.io/v3/",
    Network.OPTIMISM: "https://optimism-mainnet.infura.io/v3/",
    Network.ETHEREUM: "https://mainnet.infura.io/v3/",
    Network.BASE: "https://base-mainnet.infura.io/v3/"
}
