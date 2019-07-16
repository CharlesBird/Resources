import tushare as ts
from elasticsearch import Elasticsearch

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
stocks = sh_list_datas.to_dict(orient='records')
index = "share_datas_history-00001"
for stock in stocks:
    ts_code = stock.pop('ts_code')
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
        print(ts_code, res["hits"]["total"]["value"])