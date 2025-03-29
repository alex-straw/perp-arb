from web3 import Web3
from src.enums.enum_definitions import Contract, UniswapFee
from src.helpers.contract_helpers import get_uniswap_v3_factory_abi
from src.strategies.UniswapV3Pool import UniswapV3Pool
from src.models.data_models import ContractDTO, ERC20DTO


class UniswapV3Factory:
    def __init__(self, web3: Web3, contract_dto: ContractDTO):
        self.web3 = web3
        self.contract_dto = contract_dto
        self.smart_contract = web3.eth.contract(address=self.contract_dto.address, abi=get_uniswap_v3_factory_abi())
        self.token_a_dto = None
        self.token_b_dto = None

    def get_liquidity_pool(self, token_a_dto: ERC20DTO, token_b_dto: ERC20DTO, fee: UniswapFee = UniswapFee.FEE_3000):
        self.token_a_dto = token_a_dto
        self.token_b_dto = token_b_dto

        if self.token_a_dto.address > self.token_b_dto.address:
            self.token_a_dto, self.token_b_dto = self.token_b_dto, self.token_a_dto  # Ensure token_a < token_b (Uniswap sorting rule)

        liquidity_pool_address = self.smart_contract.functions.getPool(self.token_a_dto.address, self.token_b_dto.address, fee.value).call()

        liquidity_pool_contract = ContractDTO(Contract.UniswapV3Pool, self.contract_dto.network, liquidity_pool_address)

        return UniswapV3Pool(self.web3, liquidity_pool_contract, self.token_a_dto, self.token_b_dto)
