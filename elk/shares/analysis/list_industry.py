# 行业统计
from elasticsearch import Elasticsearch
import tushare as ts
from pprint import pprint

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

index = 'share_datas_*'

q_cnt_of_ind = {
    "size": 0,
    "aggs": {
        "count_of_industry": {
            "cardinality": {
                "field": "shareinfo.industry"
            }
        }
    }
}

res = es.search(index, body=q_cnt_of_ind)
print('去重 统计行业个数： ')
pprint(res)


q_cnt_of_per_ind = {
    "size": 0,
    "aggs": {
        "share_cnt_per_industry": {
            "terms": {
                "field": "shareinfo.industry",
                "size": 113
            }
        }
    }
}
res = es.search(index, body=q_cnt_of_per_ind)
print('每个行业股票数据个数： ')
pprint(res)


q_stats_of_per_ind = {
    "size": 0,
    "aggs": {
        "share_cnt_per_industry": {
            "terms": {
                "field": "shareinfo.industry",
                "size": 113
            },
            "aggs": {
                "stats_pct_chg": {
                    "stats": {
                        "field": "pct_chg"
                    }
                }
            }
        }
    }
}


res = es.search(index, body=q_stats_of_per_ind)
print('每个行业股票涨幅科学统计： ')
pprint(res)



