from dataclasses import dataclass

from web3 import Web3
from web3.types import ChecksumAddress
from typing import Union
from src.enums.enum_definitions import Network, Token, Contract


@dataclass
class ContractDTO:
    name: Union[Token, Contract]
    network: Network
    address: Union[str, ChecksumAddress]

    def __post_init__(self):
        self.address = Web3.to_checksum_address(self.address)

@dataclass
class ERC20DTO(ContractDTO):
    decimals: int
