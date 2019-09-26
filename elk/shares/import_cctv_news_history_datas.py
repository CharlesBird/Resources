import tushare as ts
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import time

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
index = 'news_history-cctv_news-0001'
index_failure = 'news_history-cctv_news-failure'

def insert_datas(date):
    df = pro.cctv_news(date=date)
    d_datas = df.to_dict('records')
    for data in d_datas:
        str_date = data['date'] + ' 19:00:00'
        d = datetime.strptime(str_date, '%Y%m%d %H:%M:%S')
        data['@timestamp'] = d
        data['title'] = isinstance(data['title'], str) and data['title'].strip() or ''
        data['content'] = isinstance(data['content'], str) and data['content'].strip() or ''
        del data['date']
        es.index(index=index, body=data)
        # print(data)

if __name__ == '__main__':
    start_date = datetime.strptime('20190916', '%Y%m%d')
    str_date = start_date.strftime('%Y%m%d')
    while str_date < '20190926':
        # print(str_date)
        try:
            insert_datas(str_date)
            time.sleep(0.2)
        except Exception as e:
            es.index(index=index_failure, body={'title': str_date, 'content': e})
            time.sleep(10)
        next_date = start_date + timedelta(days=1)
        str_date = next_date.strftime('%Y%m%d')
        start_date = next_date



