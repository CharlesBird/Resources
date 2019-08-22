from elasticsearch import Elasticsearch
import tushare as ts
from datetime import datetime
from pprint import pprint

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code, list_date')
stocks = sh_list_datas.to_dict('records')
for stock in stocks:
    yy = stock['list_date'][:6]
    # print(yy)
    if yy == '201908':
        print(stock)