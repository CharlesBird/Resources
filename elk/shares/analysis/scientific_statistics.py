from elasticsearch import Elasticsearch
from datetime import datetime
import time
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

res = es.search(index, body=query_of_1y)
print('一年之内科学数据统计: ')
pprint(res)

res = es.search(index, body=query_of_6M)
print('半年之内科学数据统计: ')
pprint(res)


res = es.search(index, body=query_of_3M)
print('三个月之内科学数据统计: ')
pprint(res)

res = es.search(index, body=query_of_2M)
print('两个月个月之内科学数据统计: ')
pprint(res)

res = es.search(index, body=query_of_1M)
print('一个月之内科学数据统计: ')
pprint(res)


res = es.search(index, body=query_of_1w)
print('一周之内科学数据统计: ')
pprint(res)