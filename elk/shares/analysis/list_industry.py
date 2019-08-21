# 行业统计
from elasticsearch import Elasticsearch
import tushare as ts
from pprint import pprint

es = Elasticsearch(['47.103.32.102:9200'])

TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)

index = 'share_datas_*'

# q_cnt_of_ind = {
#     "size": 0,
#     "aggs": {
#         "count_of_industry": {
#             "cardinality": {
#                 "field": "shareinfo.industry"
#             }
#         }
#     }
# }
#
# res = es.search(index, body=q_cnt_of_ind)
# print('去重 统计行业个数： ')
# pprint(res)
#
#
# q_cnt_of_per_ind = {
#     "size": 0,
#     "aggs": {
#         "share_cnt_per_industry": {
#             "terms": {
#                 "field": "shareinfo.industry",
#                 "size": 113
#             }
#         }
#     }
# }
# res = es.search(index, body=q_cnt_of_per_ind)
# print('每个行业股票数据个数： ')
# pprint(res)
#
#
# q_stats_of_per_ind = {
#     "size": 0,
#     "aggs": {
#         "share_cnt_per_industry": {
#             "terms": {
#                 "field": "shareinfo.industry",
#                 "size": 113
#             },
#             "aggs": {
#                 "stats_pct_chg": {
#                     "stats": {
#                         "field": "pct_chg"
#                     }
#                 }
#             }
#         }
#     }
# }
#
#
# res = es.search(index, body=q_stats_of_per_ind)
# print('每个行业股票涨幅科学统计： ')
# pprint(res)


# 同一个股票 存在多种行业，找出这些股票，并展示出行业名称
sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code, industry')
stock_codes = sh_list_datas.to_dict('records')
update_inds = set()
for code_dict in stock_codes:
    code = code_dict['ts_code']
    industry = code_dict['industry']
    q_ind_per_stock = {
        "size": 0,
        "aggs": {
            "count_of_industry": {
                "cardinality": {
                    "field": "shareinfo.industry",
                },
            }
        },
        "query": {
            "bool": {
                "filter": [
                    {
                        "term": {
                            'ts_code': code
                        }
                    }
                ]
            }
        }
    }
    res = es.search(index, body=q_ind_per_stock)
    # print('All shares： ')
    # pprint(res)
    cnt_inds = res['aggregations']['count_of_industry']['value']
    if cnt_inds > 1:
        update_inds.add(industry)
        update_ids = []
        # pprint(res)
        # print(code_dict)
        q_get_id = {
            "size": 1000,
            "query": {
                "term": {
                    "ts_code": code_dict['ts_code']
                }
            },
            "sort": [
                {
                    "@timestamp": "asc",
                }
            ]
        }
        res2 = es.search(index, body=q_get_id)
        for data in res2['hits']['hits']:
            update_ids.append(data['_id'])
        # pprint(res2)
        # print(code, len(res2['hits']['hits']))
        while res2['hits']['hits']:
            search_after = res2['hits']['hits'][-1]['sort']
            q_get_id = {
                "size": 1000,
                "query": {
                    "term": {
                        "ts_code": code_dict['ts_code']
                    }
                },
                "search_after": search_after,
                "sort": [
                    {
                        "@timestamp": "asc",
                    }
                ]
            }
            res2 = es.search(index, body=q_get_id)
            for data in res2['hits']['hits']:
                update_ids.append(data['_id'])
        print(update_ids)
        print(len(update_ids), code, industry)
        # es.update(index, _id, {})
            # pprint(res2)
            # print(code, len(res2['hits']['hits']))


print(update_inds)
