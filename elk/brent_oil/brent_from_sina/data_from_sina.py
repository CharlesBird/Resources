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

sem = asyncio.Semaphore(3)
# check = None
db_tables = None
hf_codes = None

async def fetch(session, url):
    async with sem:
        try:
            async with session.get(url) as resp:
                _logger.debug('url status: {}'.format(resp.status))
                if resp.status in (200, 201):
                    data = await resp.text()
                    return data
                else:
                    return ""
        except Exception as e:
            _logger.error('Get url error: {}'.format(e))
            return ""

def hanlder_data(data):
    global hf_codes
    _logger.debug('Origin data: {}'.format(data))
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
                'code': hf_codes[i],
                'change_time': change_time,
                'create_uid': 1,
                'create_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                'write_uid': 1,
                'write_date': time.strftime('%Y-%m-%d %H:%M:%S')
            })
            res.append(data_dict)
    return res

async def write_to_db(pool, q, loop):
    global hf_codes
    global db_tables
    code_table_map = dict(zip(hf_codes, db_tables))
    while True:
        _logger.debug("Queue's size: {}.".format(q.qsize()))
        if q.empty():
            await asyncio.sleep(1)
            continue
        while pool is None:
            await asyncio.sleep(1)
            _logger.warning('Reconnect to the database')
            pool = await build_db_pool(loop)
        value = await q.get()
        _logger.info('Get data from queue successfully.')
        code = value['code']
        fields = value.keys()
        fields = ','.join(fields)
        vals = value.values()
        try:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    sql = "insert into {} ({}) values {} RETURNING id".format(code_table_map[code], fields, tuple(vals))
                    await cur.execute(sql)
                    async for row in cur:
                        _logger.info('Create data {} successfully .'.format(row))
                        if row:
                            BrentWSHandler.send_message('refresh-{}'.format(code))
                            _logger.info('WS send {} message to client successfully.'.format(code))
        except Exception as e:
            _logger.error('Insert data into database table {} unsuccessfully: {}'.format(code_table_map[code], e))
            # await asyncio.sleep(1)
            # pool = await build_db_pool(loop)

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
    global hf_codes
    hf_codes = config['hf_codes'].split(',')
    code_list = []
    for code in hf_codes:
        code_list.append('hf_'+code)
    url = 'http://hq.sinajs.cn/list={}'.format(','.join(code_list))
    _logger.info('Crawl url is: {}'.format(url))
    global db_tables
    db_tables = config['db_tables'].split(',')
    _logger.info('Tables name: {}'.format(db_tables))
    assert len(hf_codes) == len(db_tables)
    check = [None] * len(db_tables)
    pool = await build_db_pool(loop)
    asyncio.ensure_future(write_to_db(pool, q, loop))
    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch(session, url)
            res = hanlder_data(data)
            _logger.debug('Processed data: {}'.format(res))
            await asyncio.sleep(0.5)
            if len(res) != len(db_tables):
                _logger.error('data size != tables size. data: {}, tables: {}'.format(res, db_tables))
                continue
            for i, r in enumerate(res):
                if check[i] and check[i] == r.get('change_time'):
                    _logger.debug('Skip duplicate data, check time is {}'.format(check[i]))
                    continue
                else:
                    check[i] = r.get('change_time')
                    await q.put(r)
                    _logger.debug('Put data to Queue: {}'.format(r))

#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     asyncio.ensure_future(main())
#     loop.run_forever()