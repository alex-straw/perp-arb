import os
from web3 import Web3


def get_infura_project_id() -> str:
    return os.getenv("INFURA_API_PROJECT_ID")


def get_infura_api_key_secret() -> str:
    return os.getenv("INFURA_API_KEY_SECRET")


def get_web3_client():
    infura_url = f"https://sepolia.infura.io/v3/{get_infura_project_id()}"
    w3 = Web3(Web3.HTTPProvider(infura_url))

    if w3.is_connected():
        return w3

    raise ConnectionError(f"Failed to connect to Ethereum node with url: {infura_url}")


def main():
    w3 = get_web3_client()


if __name__ == "__main__":
    main()
