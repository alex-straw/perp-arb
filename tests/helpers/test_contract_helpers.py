from src.helpers.contract_helpers import get_uniswap_v3_factory_abi


def test_get_abi_happy():
    abi = get_uniswap_v3_factory_abi()
    expected_abi_entry = {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"}

    assert len(abi) == 11
    assert abi[0] == expected_abi_entry
