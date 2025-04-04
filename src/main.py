from src.helpers.web3_client_helpers import get_web3_client
from src.strategies.UniswapV3Factory import UniswapV3Factory
from src.enums.enum_definitions import Network, Contract, UniswapFee
from src.models.data_models import ContractDTO, ERC20DTO


def main():
    alb_dto = ERC20DTO(Contract.ALB, Network.BASE)
    usdc_dto = ERC20DTO(Contract.USDC, Network.BASE)
    factory_dto = ContractDTO(Contract.AlienBaseUniswapV3Factory, Network.BASE)

    web3 = get_web3_client(Network.BASE)
    pool_factory = UniswapV3Factory(web3, factory_dto)

    liquidity_pool = pool_factory.get_liquidity_pool(
        alb_dto,
        usdc_dto,
        UniswapFee.FEE_10000
    )

    price = liquidity_pool.get_price()
    liquidity = liquidity_pool.get_pool_liquidity()


if __name__ == "__main__":
    main()
