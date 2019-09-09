from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import time

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
    q = {
        "size": 0,
        "aggs": {
            "stats_close": {
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
                                "gte": "2019-01-17T00:00:00.000Z",
                                "lte": "2019-07-17T23:30:00.000Z"
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
    # std_deviation = res['aggregations']['stats_close']['std_deviation']
    # if std_deviation and std_deviation < 1:
    #     print('*'*100)
    #     print('code: ', code)
    #     pprint(res['aggregations']['stats_close'])
    pprint(res)


if __name__ == '__main__':
    sh_list_datas = pro.stock_basic(exchange='', list_status='', fields='ts_code, symbol')
    stock_codes = sh_list_datas.to_dict('records')
    for stock in stock_codes:
        # print(stock)
        get_scientific_data(stock['symbol'])