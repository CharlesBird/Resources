# asyncio爬虫，去重，入库
import asyncio
import re
import aiohttp
import aiomysql
from pyquery import PyQuery

stopping = False
start_url = 'http://www.jobbole.com'
waiting_urls = []
seen_urls = set()

sem = asyncio.Semaphore(3)

async def fetch(url, session):
    async with sem:
        asyncio.sleep(1)
        try:
            async with session.get(url) as resp:
                print('url status: {}'.format(resp.status))
                if resp.status in (200, 201):
                    data = await resp.text()
                    return data
        except Exception as e:
            print(e)


def extract_urls(html):
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            waiting_urls.append(url)


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    if html is not None:
        try:
            extract_urls(html)
        except Exception as e:
            print(e, html)


async def artical_handler(url, session, pool):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            # await cur.execute("SELECT '张';")
            insert_sql = "insert into artical_test(title, url) values('{}', '{}')".format(title, url)
            await cur.execute(insert_sql)
    # pool.close()
    # await pool.wait_closed()


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waiting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waiting_urls.pop()
            print("start get url: {}".format(url))
            if re.match('^http://.*?jobbole.com/\d+/$', url):
                if url not in seen_urls:
                    asyncio.ensure_future(artical_handler(url, session, pool))
            else:
                if url and url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session))


async def main(loop):
    # 等待mysql连接建立好
    pool = await aiomysql.create_pool(host='118.190.149.30', port=3306,
                                      user='root', password='mysql',
                                      db='test', loop=loop, charset="utf8", autocommit=True)
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()