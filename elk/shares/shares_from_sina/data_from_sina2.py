import tushare as ts
from elasticsearch import Elasticsearch
from elasticsearch import helpers
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
    helpers.bulk(es, data, index=index)
    # es.index(index=index, body=data)


def main():
    # 190.34576533935595
    import time
    s = time.clock()
    get_share_datas()
    print(time.clock()-s)


if __name__ == '__main__':
    # for r in get_sina_codes():
    #     print(r)
    # main()
    # print(get_sina_codes())
    actions = [{'index': 'shares_real_time_data_2019-09-19_00001', 'doc_type': '_doc', '_source': {'code': 'sz000409', 'name': 'ST地矿', 'open': '4.730', 'yesterday_close': '4.820', 'price': '4.950', 'high': '5.060', 'low': '4.580', 'bid_price': '4.940', 'auction_price': '4.950', 'volume': '6388891', 'amount': '31123555.730', 'buy1_vol': '14974', 'buy1_quote': '4.940', 'buy2_vol': '9600', 'buy2_quote': '4.930', 'buy3_vol': '16800', 'buy3_quote': '4.920', 'buy4_vol': '35700', 'buy4_quote': '4.910', 'buy5_vol': '108500', 'buy5_quote': '4.900', 'sell1_vol': '32700', 'sell1_quote': '4.950', 'sell2_vol': '12300', 'sell2_quote': '4.960', 'sell3_vol': '29000', 'sell3_quote': '4.970', 'sell4_vol': '4800', 'sell4_quote': '4.980', 'sell5_vol': '25100', 'sell5_quote': '4.990'}}, {'index': 'shares_real_time_data_2019-09-19_00001', 'doc_type': '_doc', '_source': {'code': 'sz000410', 'name': '*ST沈机', 'open': '6.450', 'yesterday_close': '6.390', 'price': '6.460', 'high': '6.600', 'low': '6.430', 'bid_price': '6.450', 'auction_price': '6.460', 'volume': '3841985', 'amount': '24934233.610', 'buy1_vol': '44300', 'buy1_quote': '6.450', 'buy2_vol': '51300', 'buy2_quote': '6.440', 'buy3_vol': '22200', 'buy3_quote': '6.430', 'buy4_vol': '15600', 'buy4_quote': '6.420', 'buy5_vol': '36300', 'buy5_quote': '6.410', 'sell1_vol': '7000', 'sell1_quote': '6.460', 'sell2_vol': '62100', 'sell2_quote': '6.470', 'sell3_vol': '19400', 'sell3_quote': '6.480', 'sell4_vol': '12600', 'sell4_quote': '6.490', 'sell5_vol': '54900', 'sell5_quote': '6.500'}}]
    insert_into_es(actions)