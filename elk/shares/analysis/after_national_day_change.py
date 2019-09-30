from elasticsearch import Elasticsearch
from datetime import datetime,timedelta
import re
from pprint import pprint


es = Elasticsearch(['47.103.32.102:9200'])

index = 'share_datas_*'

years = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]

active_date = []
for y in years:
    start_dt = str(y) + '-10-01 15:00:00'
    search_date = start_dt.replace(' ', 'T')
    q = {
        "size": 1,
        "query": {
            "bool": {
                "filter": [
                    {
                        "term": {
                            '@timestamp': search_date
                        }
                    }
                ]
            }
        }
    }

    res = es.search(index, body=q)
    check_value = res['hits']['hits']

    while not check_value:
        next_date = datetime.strptime(start_dt, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
        next_search = next_date.strftime('%Y-%m-%dT%H:%M:%S')
        q2 = {
            "size": 1,
            "query": {
                "bool": {
                    "filter": [
                        {
                            "term": {
                                '@timestamp': next_search
                            }
                        }
                    ]
                }
            }
        }
        res2 = es.search(index, body=q2)
        check_value = res2['hits']['hits']
        start_dt = next_search.replace('T', ' ')
    active_date.append(next_search)
    # print(res)
    # pprint(res['hits']['hits'])

dd_dict = {}
gt_0 = set()
gt_3 = set()
gt_5 = set()
gt_7 = set()
for dd in active_date:
    q3 = {
        "size": 200,
        "query": {
            "bool": {
                "filter": [
                    {
                        "term": {
                            '@timestamp': dd
                        }
                    }
                ]
            }
        },
        'sort': [
            {
                '_id': 'asc'
            }
        ]
    }
    res3 = es.search(index, body=q3)
    search_after = res3['hits']['hits'][-1]['sort']
    value = res3['hits']['hits']
    for v in value:
        symbol, pct_chg = v['_source']['shareinfo']['symbol'], v['_source']['pct_chg']
        if pct_chg > 0:
            dd_dict.setdefault(dd[:4], []).append({'symbol': symbol, 'pct_chg': pct_chg})
            # print(dd, symbol, pct_chg)
    while value:
        search_after = value[-1]['sort']
        q4 = {
            "size": 200,
            "query": {
                "bool": {
                    "filter": [
                        {
                            "term": {
                                '@timestamp': dd
                            }
                        }
                    ]
                }
            },
            "search_after": search_after,
            'sort': [
                {
                    '_id': 'asc'
                }
            ]
        }
        res4 = es.search(index, body=q4)
        value = res4['hits']['hits']
        for v in value:
            symbol, pct_chg = v['_source']['shareinfo']['symbol'], v['_source']['pct_chg']
            if pct_chg > 0:
                dd_dict.setdefault(dd[:4], []).append({'symbol': symbol, 'pct_chg': pct_chg})
                # print(dd, symbol, pct_chg)
# print(dd_dict)
chg_values_18 = dd_dict['2018']
chg_values_17 = dd_dict['2017']
chg_values_16 = dd_dict['2016']
chg_values_15 = dd_dict['2015']
chg_values_14 = dd_dict['2014']
chg_values_13 = dd_dict['2013']
chg_values_12 = dd_dict['2012']
chg_values_11 = dd_dict['2011']

symbol_chg_dict = {}
for chg_value in chg_values_18:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)
for chg_value in chg_values_17:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)
for chg_value in chg_values_16:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)
for chg_value in chg_values_15:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)
for chg_value in chg_values_14:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)
for chg_value in chg_values_13:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)

for chg_value in chg_values_12:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)
for chg_value in chg_values_11:
    symbol, pct_chg = chg_value['symbol'], chg_value['pct_chg']
    symbol_chg_dict.setdefault(symbol, []).append(pct_chg)

print(symbol_chg_dict)

for symbol, per_symbol_chg in symbol_chg_dict.items():
    if len(per_symbol_chg) > 7:
        print(symbol, per_symbol_chg)
    if all(map(lambda x: x > 5, per_symbol_chg)):
        print(symbol, per_symbol_chg)