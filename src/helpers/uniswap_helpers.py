from web3 import Web3
from src.helpers.contract_helpers import get_uniswap_v3_factory_abi

UniswapV3FactoryAddress = "0x1F98431c8aD98523631AE4a59f267346ea31F984"


def get_uniswap_v3_factory_contract(w3: Web3):
    factory_address = w3.to_checksum_address(UniswapV3FactoryAddress)
    factory_contract = w3.eth.contract(address=factory_address, abi=get_uniswap_v3_factory_abi())

