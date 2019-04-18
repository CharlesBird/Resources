import asyncio
from brent_from_sina.data_from_sina import main

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(main(loop))
    asyncio.ensure_future(main(loop))
    loop.run_forever()