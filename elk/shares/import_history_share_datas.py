import tushare as ts
from elasticsearch import Elasticsearch

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

stocks = sh_list_datas.to_dict(orient='records')
for stock in stocks:
    ts_code = stock.pop('ts_code')
    df = pro.daily(ts_code=ts_code, trade_date='20190711')
    d_datas = df.to_dict('records')
    for data in d_datas:
        data.update({'shareinfo': stock, 'type': 'day'})
        es.index(index='share_datas_2019-00001', body=data)
        print(data)