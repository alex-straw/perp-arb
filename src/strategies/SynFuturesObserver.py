from web3 import Web3
from src.models.data_models import ContractDTO
from src.helpers.contract_helpers import get_syn_futures_observer_abi


class SynFuturesObserver:
    def __init__(self, web3: Web3, observer_dto: ContractDTO):
        self.web3 = web3
        self.contract_dto = observer_dto
        self.contract = web3.eth.contract(address=self.contract_dto.address, abi=get_syn_futures_observer_abi())
