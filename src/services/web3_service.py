from web3 import Web3, HTTPProvider

from src.exceptions import Web3ConnectionError
from src.models import Approval, Approvals
from src.services.helpers import get_token_name_from_address, get_amount_from_data_hex, get_64_address
from src.consts import PROVIDER_URL


class Web3Service:
    @staticmethod
    def get_address_approvals(address: str) -> Approvals:
        my_api = HTTPProvider(PROVIDER_URL)
        web3 = Web3(my_api)

        if not web3.is_connected():
            raise Web3ConnectionError()

        address_64 = get_64_address(address)

        fiter_by_event_and_address = web3.eth.filter({
            "fromBlock": "earliest",
            "toBlock": "latest",
            "topics": [
                Web3.keccak(text="Approval(address,address,uint256)"),
                address_64
            ]})

        transaction_logs = web3.eth.get_filter_logs(fiter_by_event_and_address.filter_id)

        approvals = []
        for log in transaction_logs:
            # the next line create a lot of "provider's requests", to reduce the number
            # of the requests we can save the token's names in a key-value DB (if the name is constant)
            # otherwise use dict for every address
            token_name = get_token_name_from_address(web3, log["address"])
            amount = get_amount_from_data_hex(log["data"])
            approvals.append(Approval(token_name=token_name, amount=amount))

        return Approvals(approvals=approvals)
