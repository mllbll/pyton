import asyncio

from ton import TonlibClient
from wallet_creation import wallet, wallet_address
from tonsdk.utils import to_nano

async def main():
    client = TonlibClient(config = 'https://ton.org/testnet-global.config.json')

    client.enable_unaudited_binaries()
    await client.init_tonlib(cdll_path='libtonlibjson.aarch64.so')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())