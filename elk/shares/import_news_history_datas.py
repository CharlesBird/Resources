import tushare as ts
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import time

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
index = 'news_history-news-0001'
index_failure = 'news_history-news-failure'

def insert_datas(src, start_date, end_date):
    df = pro.news(src=src, start_date=start_date, end_date=end_date, fields='datetime,content,title,channels')
    d_datas = df.to_dict('records')
    for data in d_datas:
        data['src'] = src
        if len(data['datetime']) != 19:
            d = datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M')
        else:
            d = datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S')
        data['@timestamp'] = d
        data['title'] = isinstance(data['title'], str) and data['title'].strip() or ''
        data['content'] = isinstance(data['content'], str) and data['content'].strip() or ''

        if data['channels'] and isinstance(data['channels'], list):
            channels = []
            for ch in data['channels']:
                if isinstance(ch, dict):
                    channels.append(ch['name'])
                else:
                    channels.append(ch)
            data['channels'] = channels
        del data['datetime']
        es.index(index=index, body=data)
        # print(data)


if __name__ == '__main__':
    start_date = datetime.strptime('20190820', '%Y%m%d')
    str_date1 = start_date.strftime('%Y%m%d')
    while str_date1 < '20190916':
        end_date = start_date + timedelta(days=1)
        str_date2 = end_date.strftime('%Y%m%d')
        for src in ['sina', 'wallstreetcn', '10jqka', 'eastmoney', 'yuncaijing']:
            # print(src, str_date1, str_date2)
            try:
                insert_datas(src, str_date1, str_date2)
            except Exception as e:
                es.index(index=index_failure, body={'title': str_date1, 'content': e})
                time.sleep(10)
        str_date1 = end_date.strftime('%Y%m%d')
        start_date = end_date