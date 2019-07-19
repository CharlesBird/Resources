import tushare as ts
from elasticsearch import Elasticsearch
from datetime import datetime
import time

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

fail_stocks = {}
index = "share_datas_history-00001"
fail_index = "share_datas_history_failure"

def get_stock_list():
    sh_list_datas = pro.stock_basic(exchange='', list_status='',
                                    fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

    stocks = sh_list_datas.to_dict(orient='records')
    return stocks


def get_stock_list2():
    sh_list_datas = pro.stock_basic(exchange='SSE', list_status='',
                                    fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

    stocks = sh_list_datas.to_dict(orient='records')
    new_stocks = []
    for stock in stocks:
        ts_code = stock['ts_code']
        if ts_code == '600145.SH':
            continue
        q = {
            "query": {
                "bool": {
                    "filter": [
                        {
                            "term": {
                                "ts_code": ts_code
                            }
                        },
                        {
                            "term": {
                                "@timestamp": "2019-07-12T15:00:00"
                            }
                        }
                    ]
                }
            }
        }
        res = es.search(index, body=q)
        if res["hits"]["total"]["value"] != 1:
            new_stocks.append(stock)
    return new_stocks


def get_stock_list3():
    sh_list_datas = pro.stock_basic(exchange='SSE', list_status='',
                                    fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

    stocks = sh_list_datas.to_dict(orient='records')
    res = es.search(fail_index)
    new_stocks = []
    codes = []
    for r in res['hits']['hits']:
        codes.append(r['_source']['ts_code'])
    for stock in stocks:
        if stock['ts_code'] in codes:
            new_stocks.append(stock)
    return new_stocks


def get_datas(stock):
    ts_code = stock['ts_code']
    try:
        df = pro.daily(ts_code=ts_code, start_date='20000101', end_date='20190712')
        del stock['ts_code']
    except Exception as e:
        es.index(index=fail_index, body={'ts_code': ts_code, '@timestamp': datetime.now()})
        return []
    d_datas = df.to_dict('records')
    return d_datas


def set_data(data, stock):
    data.update({'shareinfo': stock, 'type': 'day'})
    str_date = data['trade_date'] + ' 15:00:00'
    d = datetime.strptime(str_date, '%Y%m%d %H:%M:%S')
    data['@timestamp'] = d
    return data


def is_exist(data):
    trade_date = data['trade_date']
    timestamp = trade_date[:4] + '-' + trade_date[4:6] + '-' + trade_date[6:8] + 'T' + '15:00:00'
    q = {
        "query": {
            "bool": {
                "filter": [
                    {
                        "term": {
                            "ts_code": data["ts_code"]
                        }
                    },
                    {
                        "term": {
                            "@timestamp": timestamp
                        }
                    }
                ]
            }
        }
    }
    res = es.search(index, body=q)
    if res["hits"]["hits"]:
        return True
    return False


if __name__ == '__main__':
    stocks = get_stock_list3()
    for stock in stocks:
        datas = get_datas(stock)
        time.sleep(0.2)
        for data in datas:
            data = set_data(data, stock)
            es.index(index=index, body=data)
            # print(data)