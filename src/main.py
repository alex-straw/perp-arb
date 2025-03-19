import os
from web3 import Web3
from src.strategies.spot.UniswapV3Factory import UniswapV3Factory
from src.enums.network import Network
from src.enums.contract import Contract
from src.enums.token import Token
from src.enums.uniswap import UniswapFee
from src.config.addresses import CONTRACT_ADDRESSES, INFURA_NETWORKS


def get_infura_project_id() -> str:
    return os.getenv("INFURA_API_PROJECT_ID")


def get_infura_api_key_secret() -> str:
    return os.getenv("INFURA_API_KEY_SECRET")


def get_web3_client(network: Network):
    infura_url = f"{INFURA_NETWORKS[network]}{get_infura_project_id()}"
    w3 = Web3(Web3.HTTPProvider(infura_url))

    if w3.is_connected():
        return w3

    raise ConnectionError(f"Failed to connect to Ethereum node with url: {infura_url}")


def main():
    web3 = get_web3_client(Network.OPTIMISM)
    factory_address = CONTRACT_ADDRESSES[Contract.UniswapV3Factory][Network.OPTIMISM]
    pool_factory = UniswapV3Factory(web3, factory_address)

    liquidity_pool = pool_factory.get_liquidity_pool(
        CONTRACT_ADDRESSES[Token.WETH][Network.OPTIMISM],
        CONTRACT_ADDRESSES[Token.USDC][Network.OPTIMISM],
        UniswapFee.FEE_3000
    )

    print(liquidity_pool)


if __name__ == "__main__":
    main()
