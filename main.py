import asyncio
import json
from pathlib import Path

import requests
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from pytonlib.client import TonlibClient

import my_mnemonics
from ton_config import ton_conf
import os


def create_new_wallet():
    mnemonics, pub_k, priv_k, wallet = Wallets.create(WalletVersionEnum.v4r2, workchain=0)
    return mnemonics, pub_k, priv_k, wallet


def get_my_wallet(mnem):
    mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnem)
    return mnemonics, pub_k, priv_k, wallet


async def get_client():
    # try:
    ton_config = requests.get('https://ton.org/global.config.json').json()
        # create keystore directory for tonlib
    # keystore_dir = '/tmp/ton_keystore'
    keystore_dir = ""
    # Path(keystore_dir).mkdir(parents=True, exist_ok=True)


    # init TonlibClient
    client = TonlibClient(ls_index=0,  # choose LiteServer index to connect
                          config=ton_config,
                          keystore=keystore_dir)

    await client.init()
    return client
    # except requests.exceptions.ConnectionError as e:
    #     print(e)
    #     return


async def deploy_wallet():
    mnemonics_2, pub_k_2, priv_k_2, wallet_2 = get_my_wallet(my_mnemonics.mnemonics_v4)

    boc = wallet_2.create_init_external_message()['message'].to_boc(False)

    client = await get_client()
    # if client is not None:
    await client.raw_send_message(boc)

    await client.close()
    # else:
    #     print('Failed to deploy wallet.')


if __name__ == '__main__':

    client = asyncio.run(get_client())
    print()
    # asyncio.run(deploy_wallet())
    # # mnemonics, pub_k, priv_k, wallet = create_new_wallet()
    # # print(f"mnemonics: {mnemonics}")
    # # print(f"pub_k: {pub_k}")
    # # print(f"priv_k: {priv_k}")
    # # print(f"wallet: {wallet}")
    #
    # print("############################")
    # mnemonics_2, pub_k_2, priv_k_2, wallet_2 = get_my_wallet(my_mnemonics.mnemonics_v4)
    # print(f"mnemonics: {mnemonics_2}")
    # print(f"pub_k: {pub_k_2}")
    # print(f"priv_k: {priv_k_2}")
    # print(f"wallet: {wallet_2.address.to_string(True, True, True)}")

