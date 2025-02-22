import tonsdk.utils
from TonTools import Wallet, TonCenterClient

import asyncio

import my_mnemonics
from handler import TonCenterTonClient
from secret import api_key


async def main():

    # client = TonCenterClient(api_key, base_url="https://toncenter.com/api/v2/")
    client = TonCenterClient(base_url="https://toncenter.com/api/v2/")

    wallet = Wallet(provider=client, mnemonics=my_mnemonics.mnemonics_v4, version='v4r2')

    print(f"wallet address: {wallet.address}")
    print(f"wallet version: {wallet.version}")
    print(f"wallet seqno: {await wallet.get_seqno()}")
    print(f"wallet state: {await wallet.get_state()}")
    # print(f"wallet balance: {await wallet.get_balance()}")
    print(f"wallet balance: {await wallet.get_balance() / 10 ** 9} TON")
    # print(f"wallet transaction: {await wallet.get_transactions(limit_per_one_request=10)}")
    # transactions = await wallet.get_transactions()
    # print(f"wallet transaction: {transactions}")
    # print(f"wallet transaction message: {transactions[2].in_msg.msg_data}")
    # print(f"wallet transaction source: {transactions[2].in_msg.source}")
    # response_ = await wallet.transfer_ton(destination_address='UQCQCyIhLN6F2cGIrKiPlxJFl394Ni60hPEINn4gJNNJKvQf', amount=0.01, message="aref_transfer_test_2")
    # # response = await wallet.deploy()
    # print(f"response: {response_}")

    ################################################################33
    # client = TonCenterTonClient()
    # wallet = Wallet(provider=client.provider, mnemonics=my_mnemonics.mnemonics_v4, version='v4r2')
    # print(client.get_address_information(address=wallet.address))


if __name__ == '__main__':
    asyncio.run(main())
