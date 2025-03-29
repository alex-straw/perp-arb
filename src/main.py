from src.helpers.web3_client_helpers import get_web3_client
from src.strategies.UniswapV3Factory import UniswapV3Factory
from src.enums.enum_definitions import Network, Contract, UniswapFee
from src.models.data_models import ContractDTO, ERC20DTO


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
