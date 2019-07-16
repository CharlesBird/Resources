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
    sh_list_datas = pro.stock_basic(exchange='SSE', list_status='',
                                    fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

    stocks = sh_list_datas.to_dict(orient='records')
    return stocks


def get_datas(stock, try_count=0):
    ts_code = stock['ts_code']
    try:
        df = pro.daily(ts_code=ts_code, start_date='20000101', end_date='20190712')
        del stock['ts_code']
    except Exception as e:
        try_count += 1
        if try_count > 6:
            es.index(index=fail_index, body={'ts_code': ts_code})
            return []
        else:
            time.sleep(10)
            get_datas(stock, try_count)
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


def insert_into_es(data):
    es.index(index=index, body=data)


if __name__ == '__main__':
    stocks = get_stock_list()
    for stock in stocks:
        datas = get_datas(stock)
        for data in datas:
            data = set_data(data, stock)
            if not is_exist(data):
                insert_into_es(data)
            # else:
            #     print(data['ts_code'])