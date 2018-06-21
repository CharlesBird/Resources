from elasticsearch import Elasticsearch
from datetime import datetime
import time

es = Elasticsearch([{'host': '118.190.149.30', 'port': 9200}])

# 创建
# create：必须指定待查询的idnex、type、id和查询体body；缺一不可，否则报错
# index：相比于create，index的用法就相对灵活很多；id并非是一个必选项，如果指定，则该文档的id就是指定值，若不指定，则系统会自动生成一个全局唯一的id赋给该文档。
# es.create(index='test-index1', doc_type='test-type1', id='21', body={"name": "张si", "addr": "上海"})
# es.create(index='test-index2', doc_type='test-type1', id=1, body={"book": "flask", "author": "苏轼"})
# es.create(index='test-index3', doc_type='test-type3', id=2, body={"book": "flask", "author": "苏轼"})
# es.index(index='test-index1', doc_type='test-type1', body={'name': 'July', 'addr': '张家界', 'age': 26})

# 删除索引
# es.indices.delete(index='test-index1')
# 删除指定数据
# es.delete(index='test-index1', doc_type='test-type1', id='1')
# 条件删除
# query = {"query": {"match": {"name": "张si"}}}
# query = {'query': {'range': {'age': {'lt': 11}}}}
# es.delete_by_query(index='test-index1', doc_type='test-type1', body=query)

# 更新
# es.update(index='test-index1', doc_type='test-type1', id='2', body={'doc': {'addr': '深圳'}})

# 查询
# 批量条件查询
index = 'test-index1'
# query = {"query": {"match_all": {}}}
query = {"query": {"term": {"age": "19"}}}
# query = {"query": {"range": {"age": {"gt": 19}}}}
resp = es.search(index=index, body=query)
print(resp['hits']['total'])
for hit in resp['hits']['hits']:
    print(hit['_source'])
# 指定id查找
res = es.get(index=index, doc_type='test-type1', id='2')
print(res['_source'])

# 批量插入，删除，更新bulk
# doc = [
#     {'index': {'_index': 'test-index1', '_type': 'test-type1'}},
#     {'name': 'jack', 'addr': '纽约', 'age': 10},
#     {'delete': {'_index': 'test-index1', '_type': 'test-type1', '_id': '21'}},
#     {"create": {'_index': 'test-index1', "_type": 'test-type1', '_id': '3'}},
#     {'name': 'lucy', 'addr': '华盛顿', 'age': 20},
#     {'update': {'_index': 'test-index1', '_type': 'test-type1', '_id': '23'}},
#     {'doc': {'age': '100'}}
# ]
# es.bulk(index='test-index1', doc_type='test-type1', body=doc)


# match与term区别
# term是代表完全匹配，即不进行分词器分析，文档中必须包含整个搜索的词汇
# match分词查询，相当于模糊匹配,只包含其中一部分关键词就行

# term与terms
# term，查询age="20"的所有数据
print('---------term与terms-----start----------------')
query = {"query": {"term": {"age": "20"}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
# terms，查询age="18"或者age="20"的所有数据
query = {"query": {"terms": {"age": ["18", "20"]}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------term与terms-----end------------------\n')

# match与multi_match
# match，查询name包含"张"关键字
print('---------match与multi_match-----start---------')
query = {"query": {"match": {"name": "张"}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
# multi_match，查询name或者addr包含"张"关键字
query = {"query": {"multi_match": {"query": "张", "fields": ["name", "addr"]}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
# match_phrase，间隔字符数精确匹配，slop控制间隔数
query = {"query": {"match_phrase": {"name": {"query": "张", "slop": 0}}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------match与multi_match-----end-----------\n')

# ids查询
# 搜索id为2，3的所有数据
print('---------ids-----start-----------------------')
query = {"query": {"ids": {"values": ["2", "3"]}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------ids-----end-------------------------\n')

# 复合查询bool
# bool有3类查询关系，must(都满足),should(其中一个满足),must_not(都不满足)
# 获取name="jack"并且age=18的所有数据
print('---------bool-----start---------------------')
query = {"query": {"bool": {"must": [{"term": {"name": "jack"}}, {"term": {"age": 18}}]}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------bool-----end-----------------------\n')

# 切片式查询，从第2条开始，获取2条数据
print('---------from-size----start-----------------')
query = {"query": {"match_all": {}}, "from": 2, "size": 2}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------from-size-----end------------------\n')

# 范围查询，查询19<=age<=20的所有数据
print('---------range----start---------------------')
query = {"query": {"range": {"age": {"gte": 19, "lte": 20}}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------range-----end----------------------\n')

# 前缀，查询前缀为"张"的所有数据
print('---------prefix----start--------------------')
query = {"query": {"prefix": {"name": "张"}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------prefix-----end---------------------\n')

# 通配符，查询name以si为后缀的所有数据
print('---------wildcard----start------------------')
query = {"query": {"wildcard": {"name": "si"}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------wildcard-----end-------------------\n')

# 排序, 根据字段升序排序
print('---------sort----start----------------------')
query = {"query": {"match_all": {}}, "sort": {"age": {"order": "asc"}}}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------sort-----end-----------------------\n')

# filter_path
print('---------filter_path----start---------------')
# 只需要获取_id数据,多个条件用逗号隔开
res = es.search(index='test-index1', doc_type='test-type1', filter_path=['hits.hits._id'])
print(res)
# 获取所有数据
res = es.search(index='test-index1', doc_type='test-type1', filter_path=['hits.hits._*'])
print(res)
print('---------filter_path-----end----------------\n')

# count，执行查询并获取该查询的匹配数
# 获取数据量
print('---------count----start---------------------')
res = es.count(index='test-index1', doc_type='test-type1')
print(res)
print('---------count-----end----------------------\n')

# 度量类聚合，最小值，最大值，求和，平均值
print('---------aggregations----start--------------')
# 搜索所有数据，并获取age最小值
query = {
    "query": {
        "match_all": {}
    },
    "aggs": {
        "min_age": {
            "min": {
                "field": "age"
            }
        }
    }
}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
# 搜索所有数据，并获取age最大值
query = {
    "query": {
        "match_all": {}
    },
    "aggs": {
        "max_age": {
            "max": {
                "field": "age"
            }
        }
    }
}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
# 搜索所有数据，并获取所有age的和
query = {
    "query": {
        "match_all": {}
    },
    "aggs": {
        "sum_age": {
            "sum": {
                "field": "age"
            }
        }
    }
}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
# 搜索所有数据，并获取所有age的平均值
query = {
    "query": {
        "match_all": {}
    },
    "aggs": {
        "avg_age": {
            "avg": {
                "field": "age"
            }
        }
    }
}
res = es.search(index='test-index1', doc_type='test-type1', body=query)
print(res)
print('---------aggregations-----end---------------\n')