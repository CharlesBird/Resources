import asyncio
import aiomysql
# import nose


async def test_example(loop):
    pool = await aiomysql.create_pool(host='118.190.149.30', port=3306,
                                      user='root', password='mysql',
                                      db='mysql', loop=loop, charset="utf8", autocommit=True)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT '张';")
            print(cur.description)
            (r,) = await cur.fetchone()
            assert r == '张'
    pool.close()
    await pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))