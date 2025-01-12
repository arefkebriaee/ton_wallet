import tonsdk.utils
from TonTools import Wallet, TonCenterClient

import asyncio

import my_mnemonics


async def main():

    client = TonCenterClient()

    wallet = Wallet(provider=client, mnemonics=my_mnemonics.mnemonics_v4, version='v4r2')
    print(f"wallet address: {wallet.address}")
    print(f"wallet version: {wallet.version}")
    print(f"wallet seqno: {await wallet.get_seqno()}")
    print(f"wallet state: {await wallet.get_state()}")
    print(f"wallet balance: {await wallet.get_balance() / 10 ** 9}")
    # print(f"wallet transaction: {await wallet.get_transactions(limit_per_one_request=10)}")
    transactions = await wallet.get_transactions()
    print(f"wallet transaction: {transactions}")
    print(f"wallet transaction message: {transactions[1].in_msg.msg_data}")
    print(f"wallet transaction source: {transactions[1].in_msg.source}")
    response_ = await wallet.transfer_ton(destination_address=transactions[1].in_msg.source, amount=tonsdk.utils.to_nano(number=0.01, unit="ton"), message="aref_transfer_test")
    # response = await wallet.deploy()
    print(f"response: {response_}")


if __name__ == '__main__':
    asyncio.run(main())
