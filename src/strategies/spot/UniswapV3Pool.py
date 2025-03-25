from web3 import Web3
from src.helpers.contract_helpers import get_uniswap_v3_pool_abi

from src.enums.network import Network


class UniswapV3Pool:
    def __init__(self, network: Network, web3: Web3, address, token_a=None, token_b=None):
        self.web3 = web3
        self.network = network
        self.address = self.web3.to_checksum_address(address)
        self.contract = web3.eth.contract(address=self.address, abi=get_uniswap_v3_pool_abi())
        self.token_a = self.web3.to_checksum_address(token_a) if token_a is not None else None
        self.token_b = self.web3.to_checksum_address(token_b) if token_b is not None else None

    def get_pool_liquidity(self):
        return self.contract.functions.liquidity().call()

    def get_raw_price(self):
        """
        Get raw pair price/ratio ignoring decimals

        sqrtPriceX96 = sqrt(price) * 2 ** 96
        """
        slot0 = self.contract.functions.slot0().call()
        sqrt_price_x96 = slot0[0]
        price = (sqrt_price_x96 ** 2) / (2 ** 192)
        return price

