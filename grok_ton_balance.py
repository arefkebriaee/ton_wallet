import asyncio
import aiohttp
from tonsdk.utils import from_nano
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import my_mnemonics

# TON Mainnet endpoints
TONCENTER_RPC = "https://toncenter.com/api/v2"  # For balance
TONAPI_RPC = "https://tonapi.io/v2"  # For seqno


async def restore_v4r2_wallet_and_get_balance_seqno(mnemonic_list):
    # Step 1: Validate and restore the wallet
    if len(mnemonic_list) != 24:
        raise ValueError("Mnemonic list must contain exactly 24 words!")
    print("Mnemonic used:", " ".join(mnemonic_list))

    wallet_data = Wallets.from_mnemonics(
        mnemonics=mnemonic_list,
        version=WalletVersionEnum.v4r2,
        workchain=0
    )
    wallet = wallet_data[3]  # Wallet contract
    user_friendly_address = wallet.address.to_string(is_user_friendly=True)

    # Verify address
    expected_address = "UQBeobBGiRVyNzTMUXn2RJfJUAgcHdQfdHNPA4jNwKD1OqBm"
    print("Restored V4R2 Wallet Address:", user_friendly_address)
    if user_friendly_address == expected_address:
        print("SUCCESS: Address matches!")
    else:
        print("FAIL: Address does not match!")
        return

    # Step 2: Fetch balance and seqno without API key
    async with aiohttp.ClientSession() as session:
        # Fetch balance from Toncenter
        url_balance = f"{TONCENTER_RPC}/getAddressInformation?address={user_friendly_address}"
        try:
            async with session.get(url_balance) as response:
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

        url_seqno = f"{TONCENTER_RPC}/runGetMethod"

        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "address": user_friendly_address,
            "method": "seqno",
            "stack": []
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url_seqno, json=payload, headers=headers) as response:
                if response.status == 200:
                    seqno_data = await response.json()
                    if seqno_data.get("ok", False) and "result" in seqno_data:
                        try:
                            seqno = int(seqno_data["result"]["stack"][0][1], 16)  # Convert hex to int
                            print(f"Current Seqno: {seqno}")
                            # return seqno
                        except (IndexError, ValueError, KeyError):
                            print("Error parsing seqno from response:", seqno_data)
                    else:
                        print("Error in seqno response:", seqno_data.get("error", "Unknown error"))
                else:
                    print(f"Seqno HTTP Error: {response.status}")

        url_transactions = f"{TONCENTER_RPC}/getTransactions?address={user_friendly_address}&limit={seqno}"

        transaction_headers = {
            "Content-Type": "application/json"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url_transactions, headers=transaction_headers) as response:
                if response.status == 200:
                    transactions = await response.json()
                    if transactions.get("ok", False):
                        for tx in transactions:
                            print(f"Tx Hash: {tx['transaction_id']['hash']}")
                            print(f"Time: {tx['utime']}")
                            print(
                                f"In Msg: {tx['in_msg']['source']} → {tx['in_msg']['destination']}: {int(tx['in_msg']['value']) / 10 ** 9} TON")
                            print("------")
                    else:
                        print("Error in transaction response:", transactions.get("error", "Unknown error"))
                else:
                    print(f"Transactions HTTP Error: {response.status}")
        # # Fetch seqno from tonapi.io
        # url_seqno = f"{TONAPI_RPC}/accounts/{user_friendly_address}/methods/seqno"
        # # url_seqno = f"{TONCENTER_RPC}/runGetMethod?address={user_friendly_address}&method=seqno"
        #
        #
        # try:
        #     async with session.get(url_seqno) as response:
        #         if response.status == 200:
        #             seqno_data = await response.json()
        #             if seqno_data.get("ok", False) and "result" in seqno_data:
        #                 try:
        #                     seqno = int(seqno_data["result"]["stack"][0][0], 16)  # Ensure correct parsing
        #                     print(f"Current Seqno: {seqno}")
        #                 except (IndexError, ValueError, KeyError):
        #                     print("Error parsing seqno from response:", seqno_data)
        #             else:
        #                 print("Error in seqno response:", seqno_data.get("error", "Unknown error"))
        #         else:
        #             print(f"Seqno HTTP Error: {response.status}")
        # except Exception as e:
        #     print(f"Error fetching seqno: {e}")


# Run the async function
if __name__ == "__main__":
    asyncio.run(restore_v4r2_wallet_and_get_balance_seqno(my_mnemonics.mnemonics_v4))