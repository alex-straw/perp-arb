from web3 import Web3
from src.models.data_models import ContractDTO, ERC20DTO
from src.helpers.contract_helpers import get_syn_futures_observer_abi
from src.utils.math import sqrt_price_x96_to_price_syn_futures, spot_int_to_float

PERP_EXPIRY = 2**32 - 1  # Obtained from the oyster sdk


class SynFuturesObserver:
    def __init__(self, web3: Web3, observer_dto: ContractDTO):
        self.web3 = web3
        self.contract_dto = observer_dto
        self.contract = self.web3.eth.contract(address=self.contract_dto.address, abi=get_syn_futures_observer_abi())

    def read_spot_price(self, instrument_address: ContractDTO, invert=True):
        data, _block_info = self.contract.functions.getInstrumentByAddressList(
            [instrument_address.address]
        ).call()

        spot_price_int = data[0][8]

        return spot_int_to_float(spot_price_int, invert)

    def get_amm(
            self,
            instrument_address: ContractDTO,
            token_a_dto: ERC20DTO,
            token_b_dto: ERC20DTO,
            invert_price=True
    ):
        amm = self.contract.functions.getAmm(
            instrument_address.address,
            PERP_EXPIRY).call()

        ts_last = amm[1]
        sqrt_px96 = amm[4]
        oi_short = amm[7]
        oi_long = amm[9]

        if token_a_dto.address < token_b_dto.address:
            token0 = token_a_dto
            token1 = token_b_dto
        else:
            token0 = token_b_dto
            token1 = token_a_dto

        p_fair = sqrt_price_x96_to_price_syn_futures(sqrt_px96, token0, token1, is_inverse=invert_price)

        return ts_last, p_fair, oi_short, oi_long
