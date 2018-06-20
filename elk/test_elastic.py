from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch([{'host': '118.190.149.30', 'port': 9200}])

# 创建
# es.create(index='test-index1', doc_type='test-type1', id='21', body={"name": "张si", "addr": "上海"})
# es.create(index='test-index2', doc_type='test-type1', id=1, body={"book": "flask", "author": "苏轼"})
# es.create(index='test-index3', doc_type='test-type3', id=2, body={"book": "flask", "author": "苏轼"})

# 删除
# es.indices.delete(index='test-index1')

# 查询
index = 'test'
query = {"query": {"match_all": {}}}
resp = es.search()