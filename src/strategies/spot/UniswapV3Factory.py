from web3 import Web3
from src.enums.uniswap import UniswapFee
from src.enums.network import Network
from src.helpers.contract_helpers import get_uniswap_v3_factory_abi
from src.strategies.spot.UniswapV3Pool import UniswapV3Pool


class UniswapV3Factory:

    def __init__(self, network: Network, web3: Web3, address):
        self.web3 = web3
        self.network = network
        self.address = self.web3.to_checksum_address(address)
        self.contract = web3.eth.contract(address=self.address, abi=get_uniswap_v3_factory_abi())

    def get_liquidity_pool(self, token_a, token_b, fee: UniswapFee = UniswapFee.FEE_3000):
        token_a = Web3.to_checksum_address(token_a)
        token_b = Web3.to_checksum_address(token_b)

        if token_a > token_b:
            token_a, token_b = token_b, token_a  # Ensure token_a < token_b (Uniswap sorting rule)

        liquidity_pool_address = self.contract.functions.getPool(token_a, token_b, fee.value).call()

        return UniswapV3Pool(self.network, self.web3, liquidity_pool_address)
