from tonsdk.contract.wallet import Wallets, WalletVersionEnum

mnenonics = ['sail', 'garage', 'height', 'layer', 'vendor', 'win', 'fragile', 'bike', 'inch', 'parrot', 'obey', 'blouse', 'matter', 'body', 'stereo', 'agent', 'chaos', 'rigid', 'drip', 'helmet', 'minimum', 'put', 'gaze', 'thrive']


mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnenonics ,version=WalletVersionEnum.v4r2, workchain=0)

wallet_address = wallet.address.to_string(True, True, True, True)

if __name__ == '__main__':
    print(mnemonics)
    print(wallet.address.to_string(True, True, True, True))