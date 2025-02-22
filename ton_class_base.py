import asyncio
import aiohttp
from tonsdk.utils import from_nano
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import my_mnemonics

# TON Mainnet endpoints
TONCENTER_RPC = "https://toncenter.com/api/v2"  # For balance and seqno
TONAPI_RPC = "https://tonapi.io/v2"  # For transactions


class TonClient:
    def __init__(self, mnemonic_list):
        """Initialize the TonClient with a mnemonic list."""
        if len(mnemonic_list) != 24:
            raise ValueError("Mnemonic list must contain exactly 24 words!")
        print("Mnemonic used:", " ".join(mnemonic_list))

        # Restore wallet
        wallet_data = Wallets.from_mnemonics(
            mnemonics=mnemonic_list,
            version=WalletVersionEnum.v4r2,
            workchain=0
        )
        self.wallet = wallet_data[3]  # Wallet contract
        self.address = self.wallet.address.to_string(is_user_friendly=True)

        # Verify address
        expected_address = "UQBeobBGiRVyNzTMUXn2RJfJUAgcHdQfdHNPA4jNwKD1OqBm"
        print("Restored V4R2 Wallet Address:", self.address)
        if self.address == expected_address:
            print("SUCCESS: Address matches!")
        else:
            print("FAIL: Address does not match!")
            raise ValueError("Wallet address does not match expected address!")

    async def get_balance(self):
        """Fetch the wallet balance from Toncenter."""
        async with aiohttp.ClientSession() as session:
            url = f"{TONCENTER_RPC}/getAddressInformation?address={self.address}"
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get("ok", False):
                            balance_nano = int(data["result"]["balance"])
                            balance_ton = from_nano(balance_nano, unit="TON")
                            return balance_ton
                        else:
                            print("Error in balance response:", data.get("error", "Unknown error"))
                            return 0
                    else:
                        print(f"Balance HTTP Error: {response.status}")
                        return 0
            except Exception as e:
                print(f"Error fetching balance: {e}")
                return 0

    async def get_seqno(self):
        """Fetch the wallet sequence number from Toncenter using JSON-RPC."""
        async with aiohttp.ClientSession() as session:
            url = f"{TONCENTER_RPC}/jsonRPC"
            payload = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "runGetMethod",
                "params": {
                    "address": self.address,
                    "method": "seqno",
                    "stack": []
                }
            }
            try:
                async with session.post(url, json=payload) as response:
                    if response.status == 200:
                        seqno_data = await response.json()
                        if seqno_data.get("ok", False):
                            seqno = int(seqno_data["result"]["stack"][0][1], 16)  # Hex to int
                            return seqno
                        else:
                            print("Error in seqno response:", seqno_data.get("error", "Unknown error"))
                            return 0
                    else:
                        print(f"Seqno HTTP Error: {response.status}")
                        return 0
            except Exception as e:
                print(f"Error fetching seqno: {e}")
                return 0

    async def get_transaction_list(self, limit=10):
        """Fetch the wallet transaction list from tonapi.io, ordered oldest first."""
        async with aiohttp.ClientSession() as session:
            all_transactions = []
            before_lt = None  # Start with latest transactions
            while True:
                url = f"{TONAPI_RPC}/blockchain/accounts/{self.address}/transactions?limit={limit}"
                if before_lt:
                    url += f"&before_lt={before_lt}"
                try:
                    async with session.get(url) as response:
                        if response.status == 200:
                            tx_data = await response.json()
                            transactions = tx_data.get("transactions", [])
                            if not transactions:  # No more transactions
                                break
                            all_transactions.extend(transactions)
                            before_lt = transactions[-1]["lt"]  # Update to earliest lt
                        else:
                            print(f"Transactions HTTP Error: {response.status}")
                            break
                except Exception as e:
                    print(f"Error fetching transactions: {e}")
                    break

            # Reverse to match tonscan.org’s ascending order (oldest first)
            all_transactions.reverse()
            # Format transactions as a list of dictionaries
            formatted_transactions = []
            for tx in all_transactions:
                # in_msg = tx.get("in_msg", {})
                # out_msgs = tx.get("out_msgs", [])
                # formatted_tx = {
                #     "hash": tx.get("hash", "N/A"),
                #     "in_amount": from_nano(in_msg.get("value", 0), unit="TON") if in_msg else 0,
                #     "out_amount": sum(from_nano(msg.get("value", 0), unit="TON") for msg in out_msgs),
                #     "source": in_msg.get("source", "N/A") if in_msg else "N/A",
                #     "destination": out_msgs[0].get("destination", "N/A") if out_msgs else "N/A",
                #     "time": tx.get("utime", "N/A")
                # }
                formatted_transactions.append(tx)
            return formatted_transactions

    async def get_income_transactions(self, limit=10):
        """Fetch only incoming transactions (in_amount > 0) from tonapi.io, ordered oldest first."""
        all_transactions = await self.get_transaction_list(limit=limit)
        income_transactions = [tx for tx in all_transactions if from_nano(tx.get('in_msg').get("value", 0), unit="TON") > 0]
        return income_transactions


# Example usage
async def main():
    client = TonClient(my_mnemonics.mnemonics_v4)
    balance = await client.get_balance()
    print(f"Wallet Balance: {balance} TON")
    seqno = await client.get_seqno()
    print(f"Current Seqno: {seqno}")
    transactions = await client.get_transaction_list(limit=10)
    print(f"\nFound {len(transactions)} transactions (oldest first):")
    # for i, tx in enumerate(transactions):
    #     print(f"- Index {i} Hash: {tx['hash']}")
    #     print(f"  In Amount: {tx['in_amount']} TON")
    #     print(f"  Out Amount: {tx['out_amount']} TON")
    #     print(f"  Source: {tx['source']}")
    #     print(f"  Destination: {tx['destination']}")
    #     print(f"  Time: {tx['time']}")

    income_transactions = await client.get_income_transactions(limit=10)
    print(f"\nFound {len(income_transactions)} income transactions (oldest first):")
    for i, tx in enumerate(income_transactions):
        print(f"- Index {i} Hash: {tx['hash']}")
        print(f"  In Amount: {from_nano(tx.get('in_msg').get('value', 0), unit='TON') } TON")
        # print(f"  Out Amount: {tx['out_amount']} TON")
        # print(f"  Source: {tx['source']}")
        # print(f"  Destination: {tx['destination']}")
        # print(f"  Time: {tx['time']}")
        print(f"  memo: {tx.get('in_msg').get('decoded_body').get('text')}")


if __name__ == "__main__":
    asyncio.run(main())