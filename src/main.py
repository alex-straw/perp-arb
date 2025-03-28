import os
from web3 import Web3
from src.strategies.spot.UniswapV3Factory import UniswapV3Factory
from src.enums.enum_definitions import Network, Contract, UniswapFee
from src.config.addresses import CONTRACT_ADDRESSES, INFURA_NETWORKS, CONTRACT_ADDRESSES, ERC20_DECIMALS
from src.models.data_models import ContractDTO, ERC20DTO

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
    weth_dto = ERC20DTO(Contract.WETH, Network.OPTIMISM)
    usdc_dto = ERC20DTO(Contract.USDC, Network.OPTIMISM)
    factory_dto = ContractDTO(Contract.UniswapV3Factory, Network.OPTIMISM)

    web3 = get_web3_client(Network.OPTIMISM)
    pool_factory = UniswapV3Factory(web3, factory_dto)

    liquidity_pool = pool_factory.get_liquidity_pool(
        weth_dto,
        usdc_dto,
        UniswapFee.FEE_3000
    )

    print(f"Liquidity: {liquidity_pool.get_pool_liquidity()}")
    print(f"Pool Price {liquidity_pool.token_a_dto.name}/{liquidity_pool.token_b_dto.name}: {liquidity_pool.get_price()}")


if __name__ == "__main__":
    main()
