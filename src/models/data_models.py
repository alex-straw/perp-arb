from dataclasses import dataclass, field

from typing import Optional
from web3 import Web3
from web3.types import ChecksumAddress
from src.enums.enum_definitions import Network, Contract
from src.config.addresses import CONTRACT_ADDRESSES, ERC20_DECIMALS


@dataclass
class ContractDTO:
    name: Contract
    network: Network
    address: Optional[ChecksumAddress] = None

    def __post_init__(self):
        if self.address is None:
            _address = CONTRACT_ADDRESSES[self.name][self.network]
            self.address = Web3.to_checksum_address(_address)


@dataclass
class ERC20DTO(ContractDTO):
    decimals: int = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        self.decimals = ERC20_DECIMALS[self.name]
