from dataclasses import dataclass, field

from typing import Optional
from web3 import Web3
from web3.types import ChecksumAddress
from src.enums.enum_definitions import Network, Contract
from src.helpers.contract_helpers import get_contract_address, get_erc20_decimals


@dataclass
class ContractDTO:
    name: Contract
    network: Network
    address: Optional[ChecksumAddress] = None

    def __post_init__(self):
        if self.address is None:
            _address = get_contract_address(self.name, self.network)
            self.address = Web3.to_checksum_address(_address)


@dataclass
class ERC20DTO(ContractDTO):
    decimals: int = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        self.decimals = get_erc20_decimals(self.name)
