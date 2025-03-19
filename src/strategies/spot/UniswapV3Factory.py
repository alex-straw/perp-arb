from web3 import Web3
from src.enums.uniswap import UniswapFee
from src.helpers.contract_helpers import get_uniswap_v3_factory_abi


class UniswapV3Factory:

    def __init__(self, web3: Web3, factory_address):
        self.web3 = web3
        self.factory_address = self.web3.to_checksum_address(factory_address)
        self.factory_contract = web3.eth.contract(address=factory_address, abi=get_uniswap_v3_factory_abi())

    def get_liquidity_pool(self, token_a, token_b, fee: UniswapFee = UniswapFee.FEE_3000):
        token_a = Web3.to_checksum_address(token_a)
        token_b = Web3.to_checksum_address(token_b)

        if token_a > token_b:
            token_a, token_b = token_b, token_a  # Ensure token_a < token_b (Uniswap sorting rule)

        return self.factory_contract.functions.getPool(token_a, token_b, fee.value).call()
