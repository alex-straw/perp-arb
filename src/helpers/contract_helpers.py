import json
from pathlib import Path
from src.utils.path_helpers import get_project_root
from src.enums.enum_definitions import Contract, Network
from src.config.addresses import CONTRACT_ADDRESSES, ERC20_DECIMALS

ABIS_DIR = get_project_root() / "src" / "abis"
UNISWAP_V3_FACTORY_PATH = Path(ABIS_DIR) / "uniswap" / "UniswapV3Factory.json"
UNISWAP_V3_POOL_PATH = Path(ABIS_DIR) / "uniswap" / "UniswapV3Pool.json"
SYNFUTURES_OBSERVER_PATH = Path(ABIS_DIR) / "syn_futures" / "Observer.json"
SYNFUTURES_GATE_PATH = Path(ABIS_DIR) / "syn_futures" / "Gate.json"
SYNFUTURES_INSTRUMENT_PATH = Path(ABIS_DIR) / "syn_futures" / "Instrument.json"


def get_uniswap_v3_factory_abi():
    return _get_abi(UNISWAP_V3_FACTORY_PATH)


def get_uniswap_v3_pool_abi():
    return _get_abi(UNISWAP_V3_POOL_PATH)


def get_syn_futures_observer_abi():
    return _get_abi(SYNFUTURES_OBSERVER_PATH)


def get_syn_futures_gate_abi():
    return _get_abi(SYNFUTURES_GATE_PATH)


def get_syn_futures_instrument_abi():
    return _get_abi(SYNFUTURES_INSTRUMENT_PATH)


def _get_abi(path: Path):
    with open(str(path)) as abi:
        return json.load(abi)


def get_contract_address(contract: Contract, network: Network):
    try:
        return CONTRACT_ADDRESSES[contract][network]
    except KeyError as e:
        if contract not in CONTRACT_ADDRESSES:
            raise KeyError(f"Contract '{contract}' not found in CONTRACT_ADDRESSES.") from e
        if network not in CONTRACT_ADDRESSES[contract]:
            raise KeyError(f"Network '{network}' not found for contract '{contract}'.") from e


def get_erc20_decimals(contract: Contract):
    try:
        return ERC20_DECIMALS[contract]
    except KeyError as e:
        if contract not in ERC20_DECIMALS:
            raise KeyError(f"Contract '{contract}' not found in ERC20_DECIMALS.") from e