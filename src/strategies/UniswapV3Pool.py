from web3 import Web3
from src.helpers.contract_helpers import get_uniswap_v3_pool_abi
from src.models.data_models import ERC20DTO, ContractDTO


class UniswapV3Pool:
    def __init__(self, web3: Web3, pool_contract_dto: ContractDTO, token_a_dto: ERC20DTO, token_b_dto: ERC20DTO):
        self.web3 = web3
        self.contract_dto = pool_contract_dto
        self.contract = web3.eth.contract(address=self.contract_dto.address, abi=get_uniswap_v3_pool_abi())
        self.token_a_dto = token_a_dto
        self.token_b_dto = token_b_dto

    def get_pool_liquidity(self):
        return self.contract.functions.liquidity().call()

    def get_price(self):
        """
        Get price for tokenA/tokenB

        sqrtPriceX96 = sqrt(price) * 2 ** 96
        """
        slot0 = self.contract.functions.slot0().call()
        sqrt_price_x96 = slot0[0]
        price = ((sqrt_price_x96 ** 2) / (2 ** 192)) * (10 ** (self.token_a_dto.decimals - self.token_b_dto.decimals))
        return price

