from tonsdk.contract.wallet import WalletV4ContractR2
from tonsdk.crypto._mnemonic import mnemonic_to_private_key
from tonsdk.utils import to_nano
from tonsdk.provider import ToncenterClient
from tonsdk.boc import Cell
import requests

from my_mnemonics import mnemonics_v4

# Initialize TON Client (using toncenter API, replace with your own API key if needed)
TONCENTER_API_KEY = ""
ton_client = ToncenterClient("https://toncenter.com/api/v2/jsonRPC", api_key=TONCENTER_API_KEY)

keypair = mnemonic_to_private_key(mnemonics_v4)

# Initialize wallet with derived public key
w = WalletV4ContractR2(public_key=keypair[0], private_key=keypair[1])
w.create()

# Get wallet address
wallet_address = w.address.to_string(True, True, True)
print(f"Wallet Address: {wallet_address}")

# Get wallet balance
balance = ton_client.get_address_balance(wallet_address)
print(f"Wallet Balance: {balance / to_nano(1)} TON")
