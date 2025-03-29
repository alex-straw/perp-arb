import os
from web3 import Web3
from src.enums.enum_definitions import Network
from src.config.addresses import INFURA_NETWORKS


def get_infura_project_id() -> str:
    return os.getenv("INFURA_API_PROJECT_ID")


def get_infura_api_key_secret() -> str:
    return os.getenv("INFURA_API_KEY_SECRET")


def get_web3_client(network: Network):
    infura_url = f"{INFURA_NETWORKS[network]}{get_infura_project_id()}"
    w3 = Web3(Web3.HTTPProvider(infura_url))

    if w3.is_connected():
        return w3

    raise ConnectionError(f"Failed to connect to Ethereum node with url: {infura_url}")