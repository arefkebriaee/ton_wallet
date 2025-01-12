from tonsdk.contract.wallet import Wallets, WalletVersionEnum

import my_mnemonics


def create_new_wallet():
    mnemonics, pub_k, priv_k, wallet = Wallets.create(WalletVersionEnum.v3r2, workchain=0)
    return mnemonics, pub_k, priv_k, wallet


def get_my_wallet(mnem):
    mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnem)
    return mnemonics, pub_k, priv_k, wallet


if __name__ == '__main__':

    # mnemonics, pub_k, priv_k, wallet = create_new_wallet()
    # print(f"mnemonics: {mnemonics}")
    # print(f"pub_k: {pub_k}")
    # print(f"priv_k: {priv_k}")
    # print(f"wallet: {wallet}")

    print("############################")
    mnemonics_2, pub_k_2, priv_k_2, wallet_2 = get_my_wallet(my_mnemonics.my_mnemonics)
    print(f"mnemonics: {mnemonics_2}")
    print(f"pub_k: {pub_k_2}")
    print(f"priv_k: {priv_k_2}")
    print(f"wallet: {wallet_2.address.to_string(True, True, True)}")