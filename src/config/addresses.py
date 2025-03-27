from src.enums.enum_definitions import Network, Token, Contract


ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

ERC20_DECIMALS = {
    Token.WETH: 18,
    Token.USDC: 6
}

ERC20_CONTRACT_ADDRESSES = {
    Token.WETH: {
        Network.SEPOLIA: "0x7b79995e5f793A07Bc00c21412e50Ecae098E7f9",
        Network.ETHEREUM: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        Network.ARBITRUM: "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        Network.OPTIMISM: "0x4200000000000000000000000000000000000006"
    },
    Token.USDC: {
        Network.SEPOLIA: None,
        Network.ETHEREUM: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        Network.ARBITRUM: "0xFF970A61A04b1cA14834A43f5de4533eBDDB5CC8",
        Network.OPTIMISM: "0x7F5c764cBc14f9669B88837ca1490cCa17c31607"
    }
}

CONTRACT_ADDRESSES = {
    Contract.UniswapV3Factory: {
        Network.SEPOLIA: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        Network.ETHEREUM: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        Network.ARBITRUM: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        Network.OPTIMISM: "0x1F98431c8aD98523631AE4a59f267346ea31F984"
    },
    Contract.UniswapV3SwapRouter: {
        Network.SEPOLIA: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        Network.ETHEREUM: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        Network.ARBITRUM: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        Network.OPTIMISM: "0xE592427A0AEce92De3Edee1F18E0157C05861564"
    }
}


INFURA_NETWORKS = {
    Network.SEPOLIA: "https://sepolia.infura.io/v3/",
    Network.ARBITRUM: "https://arbitrum-mainnet.infura.io/v3/",
    Network.OPTIMISM: "https://optimism-mainnet.infura.io/v3/",
    Network.ETHEREUM: "https://mainnet.infura.io/v3/"
}
