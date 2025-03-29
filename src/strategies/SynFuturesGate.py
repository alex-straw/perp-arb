from web3 import Web3
from web3.types import ChecksumAddress

from typing import List

from src.helpers.contract_helpers import get_syn_futures_gate_abi
from src.models.data_models import ContractDTO


class SynFuturesGate:
    def __init__(self, web3: Web3, gate_dto: ContractDTO):
        self.web3 = web3
        self.contract_dto = gate_dto
        self.contract = web3.eth.contract(address=self.contract_dto.address, abi=get_syn_futures_gate_abi())

    def get_all_instruments(self) -> List[ChecksumAddress]:
        all_instruments = self.contract.functions.getAllInstruments().call()

        if len(all_instruments) == 0:
            return []

        return [Web3.to_checksum_address(address) for address in all_instruments]


def main():
    from src.enums.enum_definitions import Contract, Network
    from src.helpers.web3_client_helpers import get_web3_client
    web3 = get_web3_client(Network.BASE)

    gate_contract_dto = ContractDTO(Contract.SynFuturesGate, Network.BASE)
    syn_futures_gate = SynFuturesGate(web3, gate_contract_dto)

    print(syn_futures_gate.get_all_instruments())


if __name__ == "__main__":
    main()
