from src.helpers.web3_client_helpers import get_web3_client
from src.strategies.contracts.SynFuturesObserver import SynFuturesObserver
from src.strategies.contracts.UniswapV3Factory import UniswapV3Factory
from src.enums.enum_definitions import Network, Contract, UniswapFee
from src.models.data_models import ContractDTO, ERC20DTO
from src.strategies.funding_rate_arbitrage import profitability


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

    dex_price = liquidity_pool.get_price()
    # liquidity = liquidity_pool.get_pool_liquidity()

    alb = ERC20DTO(Contract.ALB, Network.BASE)
    usdc = ERC20DTO(Contract.USDC, Network.BASE)

    syn_futures_instrument_contract_dto = ContractDTO(Contract.SynFuturesInstrumentALBUSDC, Network.BASE)
    observer_contract_dto = ContractDTO(Contract.SynFuturesObserver, Network.BASE)
    syn_futures_observer = SynFuturesObserver(web3, observer_contract_dto)

    syn_futures_price = syn_futures_observer.get_instrument_price(
        syn_futures_instrument_contract_dto,
        alb,
        usdc)

    print(f"fair price / spot price = {syn_futures_price / dex_price}")

    # Estimated Profit
    profit_per_day = profitability.estimate_profit(100, syn_futures_price, dex_price, 86400)
    print(f"estimated funding rate profit for a short position per day: {profit_per_day}")


if __name__ == "__main__":
    main()
