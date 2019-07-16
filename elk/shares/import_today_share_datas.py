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
    sh_list_datas = pro.stock_basic(exchange='SZSE', list_status='',
                                    fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

    stocks = sh_list_datas.to_dict(orient='records')
    return stocks


def get_data_and_create(stocks, trade_date):
    for stock in stocks:
        ts_code = stock['ts_code']
        try:
            df = pro.daily(ts_code=ts_code, trade_date=trade_date)
            del stock['ts_code']
        except Exception as e:
            print(ts_code)
            continue
        datas = df.to_dict('records')
        for data in datas:
            data = set_data(data, stock)
            insert_into_es(data)
            # print(data)
        time.sleep(0.3)


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
    get_data_and_create(stocks, trade_date='20190716')
