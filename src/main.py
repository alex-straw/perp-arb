from src.helpers.web3_client_helpers import get_web3_client, get_block_time
from src.strategies.contracts.SynFuturesObserver import SynFuturesObserver
from src.enums.enum_definitions import Network, Contract
from src.models.data_models import ContractDTO, ERC20DTO
from src.strategies.funding_rate_arbitrage.profitability import funding_rate_per_window


def main():
    web3 = get_web3_client(Network.BASE)

    alb = ERC20DTO(Contract.ALB, Network.BASE)
    usdc = ERC20DTO(Contract.USDC, Network.BASE)

    syn_futures_instrument_contract_dto = ContractDTO(Contract.SynFuturesInstrumentALBUSDC, Network.BASE)
    observer_contract_dto = ContractDTO(Contract.SynFuturesObserver, Network.BASE)
    syn_futures_observer = SynFuturesObserver(web3, observer_contract_dto)

    ts_last, p_fair, oi_short, oi_long = syn_futures_observer.get_amm(
        syn_futures_instrument_contract_dto,
        alb,
        usdc)

    p_spot = syn_futures_observer.read_spot_price(syn_futures_instrument_contract_dto)

    t_now = get_block_time(web3)

    rate_long_1hr, rate_short_1hr = funding_rate_per_window(
        p_fair,
        p_spot,
        oi_long,
        oi_short,
        dt=int(t_now) - ts_last
    )

    notional = 100

    short_pnl_1hr = notional * rate_short_1hr

    print(f"p_fair {p_fair}")
    print(f"p_spot {p_spot}")
    print(f"Hourly funding rate long (rate_long_1h): {rate_long_1hr:.6%}")
    print(f"Hourly funding rate short (rate_short_1hr): {rate_short_1hr:.6%}")
    print(f"Expected PnL on short {notional}USDC notional: {short_pnl_1hr:.4f}USDC")


if __name__ == "__main__":
    main()
