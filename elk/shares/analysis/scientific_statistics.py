from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import time
import pandas as pd
import numpy as np

import tushare as ts
TOKEN = '137e3fc78e901b8463d68a102b168b2ea0217cb854abfad24d4dc7f7'
pro = ts.pro_api(TOKEN)
from pprint import pprint

es = Elasticsearch(['47.103.32.102:9200'])

index = 'share_datas_*'

query_of_1y = {
    "size": 0,
    "aggs": {
        "stats_close": {
            "extended_stats": {
                "field": "close"
            }
        }
    },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-1y"
                        }
                    }
                },
                {
                    "match": {
                        "shareinfo.symbol": {
                            "query": "600519"
                        }
                    }
                }
            ]
        }
    }
}

query_of_6M = {
    "size": 0,
    "aggs": {
        "stats_close": {
            "extended_stats": {
                "field": "close"
            }
        }
    },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-6M"
                        }
                    }
                },
                {
                    "match": {
                        "shareinfo.symbol": {
                            "query": "600519"
                        }
                    }
                }
            ]
        }
    }
}

query_of_3M = {
    "size": 0,
    "aggs": {
        "stats_close": {
            "extended_stats": {
                "field": "close"
            }
        }
    },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-3M"
                        }
                    }
                },
                {
                    "match": {
                        "shareinfo.symbol": {
                            "query": "600519"
                        }
                    }
                }
            ]
        }
    }
}

query_of_2M = {
    "size": 0,
    "aggs": {
        "stats_close": {
            "extended_stats": {
                "field": "close"
            }
        }
    },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-2M"
                        }
                    }
                },
                {
                    "match": {
                        "shareinfo.symbol": {
                            "query": "600519"
                        }
                    }
                }
            ]
        }
    }
}

query_of_1M = {
    "size": 0,
    "aggs": {
        "stats_close": {
            "extended_stats": {
                "field": "close"
            }
        }
    },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-1M"
                        }
                    }
                },
                {
                    "match": {
                        "shareinfo.symbol": {
                            "query": "600519"
                        }
                    }
                }
            ]
        }
    }
}

query_of_1w = {
    "size": 0,
    "aggs": {
        "stats_close": {
            "extended_stats": {
                "field": "close"
            }
        }
    },
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-1w"
                        }
                    }
                },
                {
                    "match": {
                        "shareinfo.symbol": {
                            "query": "600519"
                        }
                    }
                }
            ]
        }
    }
}

# q = {
#     "size": 0,
#     "aggs": {
#         "stats_close": {
#             "stats": {
#                 "field": "close"
#             }
#         }
#     },
#     "query": {
#         "bool": {
#             "must": [
#                 {
#                     "range": {
#                         "@timestamp": {
#                             "format": "strict_date_optional_time",
#                             "gte": "2018-08-21T01:21:43.059Z",
#                             "lte": "2019-08-21T01:21:43.059Z"
#                         }
#                     }
#                 },
#                 {
#                     "match": {
#                         "shareinfo.symbol": {
#                             "query": "600519"
#                         }
#                     }
#                 }
#             ]
#         }
#     }
# }

# res = es.search(index, body=query_of_1y)
# print('一年之内科学数据统计: ')
# pprint(res)
#
# res = es.search(index, body=query_of_6M)
# print('半年之内科学数据统计: ')
# pprint(res)
#
#
# res = es.search(index, body=query_of_3M)
# print('三个月之内科学数据统计: ')
# pprint(res)
#
# res = es.search(index, body=query_of_2M)
# print('两个月个月之内科学数据统计: ')
# pprint(res)
#
# res = es.search(index, body=query_of_1M)
# print('一个月之内科学数据统计: ')
# pprint(res)
#
#
# res = es.search(index, body=query_of_1w)
# print('一周之内科学数据统计: ')
# pprint(res)


def get_all_data(code):
    q = {
        "size": 1,
        "query": {
            "term": {
                "shareinfo.symbol": code
            }
        }
    }
    res = es.search(index, body=q)
    print(res)


def get_scientific_data(code):
    cond = {"1y": ("2018-09-10T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),
            "6m": ("2018-03-09T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),
            "5m": ("2018-04-10T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),
            "4m": ("2018-05-10T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),
            "3m": ("2018-06-10T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),
            "2m": ("2019-07-10T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),
            "1m": ("2019-08-10T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),
            "1w": ("2019-09-03T00:00:00.000Z", "2019-09-10T00:00:00.000Z"),}
    result = []
    for k, v in cond.items():
        q = {
            "size": 0,
            "aggs": {
                "stats_pct_chg": {
                    "extended_stats": {
                        "field": "pct_chg"
                    }
                }
            },
            "query": {
                "bool": {
                    "must": [
                        {
                            "range": {
                                "@timestamp": {
                                    "format": "strict_date_optional_time",
                                    "gte": v[0],
                                    "lt": v[1]
                                }
                            }
                        },
                        {
                            "match": {
                                "shareinfo.symbol": {
                                    "query": code
                                }
                            }
                        }
                    ]
                }
            }
        }
        res = es.search(index, body=q)
        # avg = res['aggregations']['stats_pct_chg']['avg']
        # std_deviation = res['aggregations']['stats_pct_chg']['std_deviation']
        # chg_value = res['aggregations']['stats_pct_chg']['sum']
        # k1 = 'std_deviation_' + k
        # k2 = 'pct_chg_' + k
        if res['aggregations']['stats_pct_chg']:
            result.extend([res['aggregations']['stats_pct_chg']['std_deviation'], res['aggregations']['stats_pct_chg']['sum']])
        else:
            return []

    return result


def get_goal_value(code, date):
    result = []
    q = {
          "query": {
              "bool": {
                  "filter": [{
                      "term": {
                          "shareinfo.symbol": code
                      }
                  },
                      {
                          "term": {
                              "@timestamp": date + "T15:00:00"
                          }
                      }]
              }
          }
    }
    res = es.search(index, body=q)
    if res['hits']['hits']:
        pct_chg = res['hits']['hits'][0]['_source']['pct_chg']
        if pct_chg > 0:
            rise = 1
        else:
            rise = 0
        result.extend([pct_chg, rise])
    return result


if __name__ == '__main__':
    sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code, symbol')
    stock_codes = sh_list_datas.to_dict('records')
    result = []
    codes = []
    for stock in stock_codes:
        # print(stock)
        goal_value = get_goal_value(stock['symbol'], "2019-09-10")
        scientific_data = get_scientific_data(stock['symbol'])
        if goal_value and scientific_data:
            result.append(goal_value+scientific_data)
            codes.append([stock['symbol']])
        # if len(result) > 10:
        #     break

    np_res = np.array(result, dtype=np.float64)
    np_codes = np.array(codes, dtype=np.object)

    df = pd.DataFrame(data=np.hstack([np_codes, np_res]), columns=['symbol', 'pct_chg', 'rise',
                                                                   'std_deviation_1y', 'pct_chg_1y',
                                                                   'std_deviation_6m', 'pct_chg_6m',
                                                                   'std_deviation_5m', 'pct_chg_5m',
                                                                   'std_deviation_4m', 'pct_chg_4m',
                                                                   'std_deviation_3m', 'pct_chg_3m',
                                                                   'std_deviation_2m', 'pct_chg_2m',
                                                                   'std_deviation_1m', 'pct_chg_1m',
                                                                   'std_deviation_1w', 'pct_chg_1w'])
    df.to_csv('./result2019-09-10.csv', index=0)