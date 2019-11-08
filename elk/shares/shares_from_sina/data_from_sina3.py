import tushare as ts
from elasticsearch import Elasticsearch
import re
import requests
from datetime import datetime
TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
es = Elasticsearch(['47.103.32.102:9200'])

index = "shares_real_time_data_2019-09-19_00001"


def all_shares_codes():
    sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol')
    return sh_list_datas.to_dict('records')


def get_sina_codes(step=500):
    shares_list = all_shares_codes()
    start = 0
    sina_codes = []
    while shares_list[start:start + step]:
        per_codes = []
        for share in shares_list[start:start + step]:
            if share['ts_code'][-2:] == 'SH':
                per_codes.append('sh' + share['symbol'])
            elif share['ts_code'][-2:] == 'SZ':
                per_codes.append('sz' + share['symbol'])
            else:
                pass
        sina_codes.append(per_codes)
        start += step
    return sina_codes


def get_share_datas():
    sina_codes = get_sina_codes()
    for codes in sina_codes:
        url = 'http://hq.sinajs.cn/list={}'.format(','.join(codes))
        response = requests.get(url)
        data = response.text
        pattern = re.compile('="(.*)"')
        data_list = pattern.findall(data)
        for i, str_data in enumerate(data_list):
            code = codes[i]
            list_data = str_data.split(',')
            features = ['name', 'open', 'yesterday_close', 'price', 'high', 'low', 'bid_price', 'auction_price',
                        'volume', 'amount', 'buy1_vol', 'buy1_quote', 'buy2_vol', 'buy2_quote', 'buy3_vol',
                        'buy3_quote', 'buy4_vol', 'buy4_quote', 'buy5_vol', 'buy5_quote', 'sell1_vol', 'sell1_quote',
                        'sell2_vol', 'sell2_quote', 'sell3_vol', 'sell3_quote', 'sell4_vol', 'sell4_quote', 'sell5_vol',
                        'sell5_quote']
            value = {'code': code}
            for j, f in enumerate(features):
                value.update({f: list_data[j]})
            date = list_data[30]
            date_t = list_data[31]
            str_date = date + ' ' + date_t
            d = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
            value.update({'@timestamp': d})
            print(value)
            insert_into_es(value)


def insert_into_es(data):
    es.index(index=index, body=data)


def main():
    # 190.34576533935595
    # 110.30940818305449
    import time
    s = time.clock()
    get_share_datas()
    print(time.clock()-s)


if __name__ == '__main__':
    # for r in get_sina_codes():
    #     print(r)
    main()
    # print(get_sina_codes())