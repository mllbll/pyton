import asyncio

from TonTools import TonCenterClient, Wallet
from wallet_creation import mnemonics


async def main():
    provider = TonCenterClient(base_url='https://ton.org/testnet-global.congigs.json')
    wallet = Wallet(mnemonics = mnemonics, provider=provider)

    await wallet.transfer_ton(destination_address='EQAFmjUoZUqKFEBGYFEMbv-m61sFStgAfUR8J6hJDwUU09iT',
                              amount=0.01, message = 'Hello from Ivan')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())