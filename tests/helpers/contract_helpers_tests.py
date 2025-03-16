import unittest
from src.helpers.contract_helpers import get_uniswap_v3_factory_abi


class ContractHelpersTests(unittest.TestCase):
    def test_get_abi_happy(self):
        abi = get_uniswap_v3_factory_abi()
        expected_abi_entry = {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"}

        self.assertEqual(len(abi), 11)
        self.assertEqual(abi[0], expected_abi_entry)


if __name__ == '__main__':
    unittest.main()
