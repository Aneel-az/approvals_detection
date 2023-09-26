from ast import literal_eval

from hexbytes import HexBytes
from web3 import Web3

from src.consts import ABI


def get_token_name_from_address(web3: Web3, token_address: str) -> str:
    return web3.eth.contract(address=token_address, abi=ABI).functions.name().call()


def get_amount_from_data_hex(data_hex: HexBytes) -> int:
    data_hex_str = data_hex.hex()
    return literal_eval(data_hex_str)


def get_64_address(address: str) -> str:
    prefix, address_without_prefix = address[:2], address[2:]
    zeros_to_add = 64 - len(address_without_prefix)
    return f'{prefix}{"0"*zeros_to_add}{address_without_prefix}'
