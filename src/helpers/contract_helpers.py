import json
from pathlib import Path
from src.utils.path_helpers import get_project_root

ABIS_DIR = get_project_root() / "src" / "abis"
UNISWAP_V3_FACTORY_PATH = Path(ABIS_DIR) / "uniswap" / "UniswapV3Factory.json"
UNISWAP_V3_POOL_PATH = Path(ABIS_DIR) / "uniswap" / "UniswapV3Pool.json"


def get_uniswap_v3_factory_abi():
    return _get_abi(UNISWAP_V3_FACTORY_PATH)


def get_uniswap_v3_pool_abi():
    return _get_abi(UNISWAP_V3_POOL_PATH)


def _get_abi(path: Path):
    with open(str(path)) as abi:
        return json.load(abi)
