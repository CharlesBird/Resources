import re
import time
import asyncio
import aiohttp
import aiopg
from asyncio import Queue
from .tools import config
from .wsserver import BrentWSHandler
import logging
_logger = logging.getLogger(__name__)

q = Queue()
url = 'http://hq.sinajs.cn/list=hf_OIL'

sem = asyncio.Semaphore(3)
check = None

async def fetch(session, url):
    async with sem:
        try:
            async with session.get(url) as resp:
                _logger.debug('url status: {}'.format(resp.status))
                if resp.status in (200, 201):
                    data = await resp.text()
                    return data
        except Exception as e:
            _logger.error('Get url error: {}'.format(e))

def hanlder_data(data):
    _logger.debug('Origin data: {}'.format(data))
    pattern = re.compile('="(.*)"')
    s = pattern.findall(data)
    res = {}
    if s:
        s_l = s[0].split(',')
        change_time = ' '.join([s_l[12], s_l[6]])
        res.update({
            'last_price': float(s_l[0]),
            'change_value': round(float(s_l[0]) - float(s_l[7]), 2),
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
            'change_time': change_time,
            'create_uid': 1,
            'create_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'write_uid': 1,
            'write_date': time.strftime('%Y-%m-%d %H:%M:%S')
        })
    return res

async def write_to_db(pool, q, loop):
    while True:
        _logger.debug("Queue's size: {}.".format(q.qsize()))
        if q.empty():
            await asyncio.sleep(0.5)
            continue
        while pool is None:
            await asyncio.sleep(1)
            _logger.warning('Reconnect to the database')
            pool = await build_db_pool(loop)
        value = await q.get()
        _logger.info('Get data from queue successfully.')
        fields = value.keys()
        fields = ','.join(fields)
        vals = value.values()
        try:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    sql = "insert into {} ({}) values {} RETURNING id".format(config['db_table'], fields, tuple(vals))
                    await cur.execute(sql)
                    async for row in cur:
                        _logger.info('Create data {} successfully .'.format(row))
                        if row:
                            BrentWSHandler.send_message('refresh')
                            _logger.info('WS send message to client successfully.')
        except Exception as e:
            _logger.error('Insert data into database unsuccessfully: {}'.format(e))
            await asyncio.sleep(1)
            pool = await build_db_pool(loop)

async def build_db_pool(loop):
    try:
        dns = 'dbname={} user={} password={} host={} port={}'.format(config['db_name'], config['db_user'],
                                                                     config['db_password'], config['db_host'],
                                                                     config['db_port'])
        pool = await aiopg.create_pool(dns, loop=loop)
        _logger.info('Successful connect to database {}.'.format(config['db_name']))
    except Exception as e:
        _logger.error('Unable to connect to the database: {}'.format(e))
        pool = None
    return pool

async def main(loop):
    config.parse_config()
    _logger.info('Script Start..')
    pool = await build_db_pool(loop)
    asyncio.ensure_future(write_to_db(pool, q, loop))
    global check
    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch(session, url)
            res = hanlder_data(data)
            _logger.debug('Processed data: {}'.format(res))
            await asyncio.sleep(0.5)
            if check and check == res.get('change_time'):
                _logger.debug('Skip duplicate data, check time is {}'.format(check))
                continue
            else:
                check = res.get('change_time')
                await q.put(res)
                _logger.debug('Put data to Queue: {}'.format(res))

#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     asyncio.ensure_future(main())
#     loop.run_forever()