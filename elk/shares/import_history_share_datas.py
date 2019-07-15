import tushare as ts
from elasticsearch import Elasticsearch
from datetime import datetime
import time

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

stocks = sh_list_datas.to_dict(orient='records')
index = "share_datas_history-00001"
for stock in stocks:
    ts_code = stock.pop('ts_code')
    print(ts_code)
    # df = pro.daily(ts_code=ts_code, start_date='20000101')
    df = pro.daily(ts_code=ts_code, trade_date='20190715')
    d_datas = df.to_dict('records')
    for data in d_datas:
        data.update({'shareinfo': stock, 'type': 'day'})
        str_date = data['trade_date'] + ' 15:00:00'
        d = datetime.strptime(str_date, '%Y%m%d %H:%M:%S')
        data['@timestamp'] = d
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
                        "@timestamp": "2019-07-15T15:00:00"
                      }
                    }
                  ]
                }
              }
            }
        res = es.search(index, body=q)
        print(res["hits"]["hits"])
        # if not res["hits"]["hits"]:
        #     es.index(index=index, body=data)
        # print(data)
        # es.index(index=index, body=data)
    time.sleep(0.3)