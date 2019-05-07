import re
import time
import asyncio
import aiohttp
import aiopg
from asyncio import Queue

q = Queue()
url = 'http://hq.sinajs.cn/list=hf_OIL,hf_CL'

sem = asyncio.Semaphore(3)
check = [None] * 2
hf_codes = ['OIL', 'CL']

async def fetch(session, url):
    async with sem:
        try:
            async with session.get(url) as resp:
                # print('url status: {}'.format(resp.status))
                if resp.status in (200, 201):
                    data = await resp.text()
                    return data
        except Exception as e:
            print(e)

def hanlder_data(data):
    pattern = re.compile('="(.*)"')
    s_list = pattern.findall(data)
    res = []
    for i, s in enumerate(s_list):
        data_dict = {}
        if s:
            s_l = s.split(',')
            change_time = ' '.join([s_l[12], s_l[6]])
            data_dict.update({
                'last_price': float(s_l[0]),
                'change_value': float(s_l[1]),
                'buy_price': float(s_l[2]),
                'sell_price': float(s_l[3]),
                'max_price': float(s_l[4]),
                'min_price': float(s_l[5]),
                'yestoday_price': float(s_l[7]),
                'open_price': float(s_l[8]),
                'amount': float(s_l[9]),
                'buy_amount': float(s_l[10]),
                'sell_amount': float(s_l[11]),
                'name': s_l[13],
                'code': hf_codes[i],
                'change_time': change_time,
                'create_uid': 1,
                'create_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                'write_uid': 1,
                'write_date': time.strftime('%Y-%m-%d %H:%M:%S')
            })
            res.append(data_dict)
    return res

async def write_to_db(pool, q):
    while True:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                if q.empty():
                    await asyncio.sleep(0.5)
                value = await q.get()
                fields = value.keys()
                fields = ','.join(fields)
                vals = value.values()
                print(fields, vals)
                # sql = "insert into brent_oil_record ({}) values {} RETURNING id".format(fields, tuple(vals))
                # await cur.execute(sql)

async def main():
    global check
    pool = await aiopg.create_pool('dbname=CCCC0226 user=ccerp password='' host=127.0.0.1')
    asyncio.ensure_future(write_to_db(pool, q))
    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch(session, url)
            res = hanlder_data(data)
            # print(res)
            await asyncio.sleep(0.5)
            assert len(res) == 2
            for i, r in enumerate(res):
                if check[i] and check[i] == r.get('change_time'):
                    continue
                else:
                    check[i] = r.get('change_time')
                    await q.put(r)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()