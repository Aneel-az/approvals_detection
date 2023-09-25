from web3 import Web3, HTTPProvider

from src.utils import get_token_name_from_address, get_amount_from_data_hex, get_64_address


def get_address_approvals(address: str):
    my_api = HTTPProvider("https://mainnet.infura.io/v3/a473799e1e1a4966bc5ca9a571e8b4e0")
    web3 = Web3(my_api)

    if not web3.is_connected():
        print("failed to connect to the blockchain")
        return

    address_64 = get_64_address(address)

    fiter_by_event_and_address = web3.eth.filter({
        "fromBlock": "earliest",
        "toBlock": "latest",
        "topics": [
            Web3.keccak(text="Approval(address,address,uint256)"),
            address_64
        ]})

    transaction_logs = web3.eth.get_filter_logs(fiter_by_event_and_address.filter_id)
    for log in transaction_logs:
        token_name = get_token_name_from_address(web3, log["address"])
        amount = get_amount_from_data_hex(log["data"])
        print(f"approval on {token_name} on amount of {amount}")
