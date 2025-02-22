# import asyncio
# import aiohttp
# from tonsdk.utils import from_nano
# from tonsdk.contract.wallet import Wallets, WalletVersionEnum
#
# import my_mnemonics
#
# # TON Mainnet RPC endpoint
# MAINNET_RPC = "https://toncenter.com/api/v2"
#
#
# async def restore_v4r2_wallet_and_get_balance(mnemonic_list):
#     # Step 1: Validate and restore the wallet
#     if len(mnemonic_list) != 24:
#         raise ValueError("Mnemonic list must contain exactly 24 words!")
#     print("Mnemonic used:", " ".join(mnemonic_list))
#
#     wallet_data = Wallets.from_mnemonics(
#         mnemonics=mnemonic_list,
#         version=WalletVersionEnum.v4r2,
#         workchain=0
#     )
#     wallet = wallet_data[3]  # Wallet contract
#     user_friendly_address = wallet.address.to_string(is_user_friendly=True)
#
#     # Verify address
#     expected_address = "UQBeobBGiRVyNzTMUXn2RJfJUAgcHdQfdHNPA4jNwKD1OqBm"
#     print("Restored V4R2 Wallet Address:", user_friendly_address)
#     if user_friendly_address == expected_address:
#         print("SUCCESS: Address matches!")
#     else:
#         print("FAIL: Address does not match!")
#         return
#
#     # Step 2: Fetch balance without API key
#     async with aiohttp.ClientSession() as session:
#         url = f"{MAINNET_RPC}/getAddressInformation?address={user_friendly_address}"
#         try:
#             async with session.get(url) as response:
#                 if response.status == 200:
#                     data = await response.json()
#                     if data.get("ok", False):
#                         balance_nano = int(data["result"]["balance"])
#                         balance_ton = from_nano(balance_nano, unit="TON")  # Defaults to TON
#                         print(f"Wallet Balance: {balance_ton} TON")
#                     else:
#                         print("Error in response:", data.get("error", "Unknown error"))
#                 else:
#                     print(f"HTTP Error: {response.status}")
#         except Exception as e:
#             print(f"Error fetching balance: {e}")
#
#
# # Run the async function
# if __name__ == "__main__":
#     asyncio.run(restore_v4r2_wallet_and_get_balance(my_mnemonics.mnemonics_v4))


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

        # Fetch seqno from tonapi.io
        url_seqno = f"{TONAPI_RPC}/accounts/{user_friendly_address}/methods/seqno"
        try:
            async with session.get(url_seqno) as response:
                if response.status == 200:
                    seqno_data = await response.json()
                    seqno = seqno_data.get("result", {}).get("stack", [{}])[0].get("number", 0)
                    print(f"Current Seqno: {seqno}")
                else:
                    print(f"Seqno HTTP Error: {response.status}")
        except Exception as e:
            print(f"Error fetching seqno: {e}")


# Run the async function
if __name__ == "__main__":
    asyncio.run(restore_v4r2_wallet_and_get_balance_seqno(my_mnemonics.mnemonics_v4))