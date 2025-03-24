from web3 import Web3
from src.helpers.contract_helpers import get_uniswap_v3_pool_abi

from src.enums.network import Network


class UniswapV3Pool:
    def __init__(self, network: Network, web3: Web3, address):
        self.web3 = web3
        self.network = network
        self.address = self.web3.to_checksum_address(address)
        self.contract = web3.eth.contract(address=address, abi=get_uniswap_v3_pool_abi())

