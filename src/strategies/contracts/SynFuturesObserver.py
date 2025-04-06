from web3 import Web3
from src.models.data_models import ContractDTO, ERC20DTO
from src.helpers.contract_helpers import get_syn_futures_observer_abi
from src.utils.math import sqrt_price_x96_to_price_syn_futures

PERP_EXPIRY = 2**32 - 1  # Obtained from the oyster sdk

RATIO_BASE = 10_000

IMR_STEP_RATIO_MAP = {
    100: [5, 10, 15],
    300: [5, 15, 35],
    500: [5, 25, 50],
    1000: [5, 50, 100],
}

TICK_DELTA_MAX = 16096  # 1.0001 ** 16096 = 5.0004080813

# A tick represents a discrete unit of price movement in the AMM.
# The price is calculated as: price = 1.0001^tick
# So, a tickDelta defines how wide a range around the current price we want to scan.
# For example, a tickDelta of 953 means scanning ±953 ticks, or approximately ±10% in price terms,
# since 1.0001^953 ≈ 1.1 (a 10% increase) and 1.0001^-953 ≈ 0.91 (a 10% decrease).

TICK_DELTA = 953  # Covers roughly ±10% price range around the current AMM tick


class SynFuturesObserver:
    def __init__(self, web3: Web3, observer_dto: ContractDTO):
        self.web3 = web3
        self.contract_dto = observer_dto
        self.contract = web3.eth.contract(address=self.contract_dto.address, abi=get_syn_futures_observer_abi())

    def get_instrument_price(
            self,
            instrument_address: ContractDTO,
            token_a_dto: ERC20DTO,
            token_b_dto: ERC20DTO
    ):
        liquidity_details = self.contract.functions.liquidityDetails(
            instrument_address.address,
            PERP_EXPIRY,
            TICK_DELTA
        ).call()

        if token_a_dto.address < token_b_dto.address:
            token0 = token_a_dto
            token1 = token_b_dto
        else:
            token0 = token_b_dto
            token1 = token_a_dto

        amm = liquidity_details[0]
        sqrt_price_x96 = amm[0]

        return sqrt_price_x96_to_price_syn_futures(sqrt_price_x96, token0, token1, is_inverse=True)


def main():
    from src.enums.enum_definitions import Contract, Network
    from src.helpers.web3_client_helpers import get_web3_client
    web3 = get_web3_client(Network.BASE)

    alb = ERC20DTO(Contract.ALB, Network.BASE)
    usdc = ERC20DTO(Contract.USDC, Network.BASE)

    syn_futures_instrument_contract_dto = ContractDTO(Contract.SynFuturesInstrumentALBUSDC, Network.BASE)
    observer_contract_dto = ContractDTO(Contract.SynFuturesObserver, Network.BASE)
    syn_futures_observer = SynFuturesObserver(web3, observer_contract_dto)

    price = syn_futures_observer.get_instrument_price(
        syn_futures_instrument_contract_dto,
        alb,
        usdc)


if __name__ == "__main__":
    main()
