from TonTools import Wallet, TonCenterClient

import asyncio

import my_mnemonics


async def main():

    client = TonCenterClient()

    wallet = Wallet(provider=client, mnemonics=my_mnemonics.mnemonics_v4, version='v4r2')
    print(f"wallet address: {wallet.address}")
    print(f"wallet version: {wallet.version}")
    print(f"wallet state: {await wallet.get_state()}")
    print(f"wallet balance: {await wallet.get_balance()}")
    response = await wallet.deploy()
    print(f"response: {response}")


if __name__ == '__main__':
    asyncio.run(main())
