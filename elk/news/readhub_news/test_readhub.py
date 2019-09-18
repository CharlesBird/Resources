import requests
import jieba
from pprint import pprint

start_url = 'https://api.readhub.cn/topic?lastCursor={}&pageSize=20'
url = start_url.format('')
res = requests.get(url)
data = res.json()['data']
pprint(data)
while data:
    for r in data:
        # print(r['order'])
        # print(r['title'])
        # print(r['summary'])
        seg_list = jieba.cut_for_search(r['summary'])

        print(", ".join(seg_list))
    last_order = r['order']
    print(last_order)
    url = start_url.format(last_order)
    res = requests.get(url)
    data = res.json()['data']