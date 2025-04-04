from web3 import Web3
from src.helpers.contract_helpers import get_uniswap_v3_pool_abi
from src.models.data_models import ERC20DTO, ContractDTO
from src.utils.math import sqrt_price_x96_to_price


class UniswapV3Pool:
    def __init__(self, web3: Web3, pool_contract_dto: ContractDTO, token_a_dto: ERC20DTO, token_b_dto: ERC20DTO):
        self.web3 = web3
        self.contract_dto = pool_contract_dto
        self.contract = web3.eth.contract(address=self.contract_dto.address, abi=get_uniswap_v3_pool_abi())

        if token_a_dto.address < token_b_dto.address:
            self.token0 = token_a_dto
            self.token1 = token_b_dto
        else:
            self.token0 = token_b_dto
            self.token1 = token_a_dto

    def get_pool_liquidity(self):
        liquidity = self.contract.functions.liquidity().call()
        print(f"Liquidity: ({self.token0.name.value}/{self.token1.name.value}) {liquidity}")
        return liquidity

    def get_price(self):
        """
        Get price for tokenA/tokenB

        sqrtPriceX96 = sqrt(price) * 2 ** 96
        """
        slot0 = self.contract.functions.slot0().call()
        sqrt_price_x96 = slot0[0]
        price = sqrt_price_x96_to_price(sqrt_price_x96, self.token0, self.token1)
        return price

