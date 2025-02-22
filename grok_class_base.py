import asyncio
from selectors import SelectSelector

import aiohttp
from tonsdk.utils import from_nano, Address, bytes_to_b64str
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

from my_mnemonics import mnemonics_v4

# from watcher.secret import mnemonics_v4

# TON Mainnet endpoints
TONCENTER_RPC = "https://toncenter.com/api/v2"  # For balance
TONAPI_RPC = "https://tonapi.io/v2"  # For seqno and transactions

class TonClient:

    def __init__(self, mnemonic_list: list):
        wallet_data = Wallets.from_mnemonics(
            mnemonics=mnemonic_list,
            version=WalletVersionEnum.v4r2,
            workchain=0
        )
        self.wallet = wallet_data[3]
        self.address = self.wallet.address.to_string(is_user_friendly=True)
        self.url_balance = f"{TONCENTER_RPC}/getAddressInformation?address={self.address}"

    def convert_to_user_friendly(self, raw_address: str):
        # Create Address object
        address_obj = Address(raw_address)

        # Convert to user-friendly format
        user_friendly_address = address_obj.to_string(is_user_friendly=True)

        return user_friendly_address


    # async def restore_v4r2_wallet_and_get_balance_seqno(self, mnemonic_list):
        # Step 1: Validate and restore the wallet
        # if len(mnemonic_list) != 24:
        #     raise ValueError("Mnemonic list must contain exactly 24 words!")
        # print("Mnemonic used:", " ".join(mnemonic_list))
        #
        # wallet_data = Wallets.from_mnemonics(
        #     mnemonics=mnemonic_list,
        #     version=WalletVersionEnum.v4r2,
        #     workchain=0
        # )
        # self.wallet = wallet_data[3]  # Wallet contract
        # user_friendly_address = self.wallet.address.to_string(is_user_friendly=True)
        #
        # # Verify address
        # expected_address = "UQBeobBGiRVyNzTMUXn2RJfJUAgcHdQfdHNPA4jNwKD1OqBm"
        # print("Restored V4R2 Wallet Address:", user_friendly_address)
        # if user_friendly_address == expected_address:
        #     print("SUCCESS: Address matches!")
        # else:
        #     print("FAIL: Address does not match!")
        #     return


    async def get_balance(self):
        # Step 2: Fetch balance, seqno, and transactions without API key
        # with aiohttp.ClientSession() as session:
            # Fetch balance from Toncenter
            # url_balance = f"{TONCENTER_RPC}/getAddressInformation?address={self.address}"
        try:
            with aiohttp.ClientSession().get(self.url_balance) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("ok", False):
                        balance_nano = int(data["result"]["balance"])
                        balance_ton = from_nano(balance_nano, unit="TON")
                        print(f"Wallet Balance: {balance_ton} TON")
                    else:
                        print("Error in balance response:", data.get("error", "Unknown error"))
                else:
                    print(f"Balance HTTP Error: {response.status}")
        except Exception as e:
            print(f"Error fetching balance: {e}")

    async def get_seqno(self):
            # Fetch seqno from tonapi.io (your working solution)
            url_seqno = f"{TONAPI_RPC}/accounts/{self.address}/methods/seqno"
            try:
                with aiohttp.ClientSession().get(url_seqno) as response:
                    if response.status == 200:
                        seqno_data = await response.json()
                        seqno = seqno_data.get("result", {}).get("stack", [{}])[0].get("number", 0)
                        print(f"Current Seqno: {seqno}")
                    else:
                        print(f"Seqno HTTP Error: {response.status}")
            except Exception as e:
                print(f"Error fetching seqno: {e}")

    async def get_transaction_list(self):
            # Fetch transactions from tonapi.io
            url_transactions = f"{TONAPI_RPC}/blockchain/accounts/{self.address}/transactions?limit=10"
            try:
                async with aiohttp.ClientSession().get(url_transactions) as response:
                    if response.status == 200:
                        tx_data = await response.json()
                        transactions = tx_data.get("transactions", [])
                        print(f"\nFound {transactions} transactions:")
                        for index, tx in enumerate(transactions):

                            tx_hash = tx.get("hash", "N/A")
                            amount = from_nano(tx.get("total_fees", 0), unit="TON")  # Total fees as an example
                            # For in/out amounts, check 'in_msg' and 'out_msgs'
                            in_msg = tx.get("in_msg", {})
                            out_msgs = tx.get("out_msgs", [])
                            in_amount = from_nano(in_msg.get("value", 0), unit="TON") if in_msg else 0
                            out_amount = sum(from_nano(msg.get("value", 0), unit="TON") for msg in out_msgs)
                            source = in_msg.get("source", "N/A") if in_msg else "N/A"
                            destination = out_msgs[0].get("destination", "N/A") if out_msgs else "N/A"
                            time = tx.get("utime", "N/A")
                            # message = tx['out_msgs'][0]['decoded_body']['text'] if in_amount == 0 else "no message"
                            if in_amount != 0:
                                message = tx.get("in_msg").get('decoded_body').get('text')
                                print("\n")
                                print(f"TX: {index + 1}:\n  hash: {tx_hash}\n   in amount: {in_amount} TON\n    out amount: {out_amount} TON\nsource: {self.convert_to_user_friendly(in_msg.get('source').get('address'))}\n  destination: {self.convert_to_user_friendly(in_msg.get('destination').get('address'))}\n  message: {message}")
                            # print(f"- Hash: {tx['hash']}")
                            # print(f"  In Amount: {in_amount} TON")
                            # print(f"  Out Amount: {out_amount} TON")
                            # print(f"  Source: {source}")
                            # print(f"  Destination: {destination}")
                            # print(f"  Time: {time}")
                    else:
                        print(f"Transactions HTTP Error: {response.status}")
            except Exception as e:
                print(f"Error fetching transactions: {e}")


# Run the async function
if __name__ == "__main__":
    # asyncio.run(restore_v4r2_wallet_and_get_balance_seqno(my_mnemonics.mnemonics_v4))
    ton_client = TonClient(mnemonic_list=mnemonics_v4)
    print(f"wallet_address: {ton_client.address}")
    print(f"balance: {ton_client.get_balance()}")