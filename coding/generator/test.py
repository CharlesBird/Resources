import asyncio
import aiopg
from queue import Queue


async def build_db_pool(loop):
    try:
        dns = 'dbname={} user={} password={} host={} port={}'.format('CCCC02216', 'ccerp',
                                                                     '', '127.0.0.1', 5432)
        pool = await aiopg.create_pool(dns, loop=loop)
    except Exception as e:
        print('Unable to connect.{}'.format(e))
        pool = None
    return pool


async def write_to_db(pool, loop):
    while True:
        try:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("select 1;")
                    async for row in cur:
                        print(row)
        except Exception as e:
            await asyncio.sleep(3)
            print(12123214234)
            pool = await build_db_pool(loop)

async def main(loop):
    pool = await build_db_pool(loop)
    asyncio.ensure_future(write_to_db(pool, loop))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(main(loop))
    asyncio.ensure_future(main(loop))
    loop.run_forever()