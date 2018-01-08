from pymongo import MongoClient
from elasticsearch import Elasticsearch

_db = MongoClient('mongodb://127.0.0.1:27017')['blog']
print(_db)
_es = Elasticsearch()
print(_es)

_index_mappings = {
    "mappings": {
        "user": {
            "properties": {
                "title": {"type": "text"},
                "name": {"type": "text"},
                "age": {"type": "integer"}
            }
        },
        "blogpost": {
            "properties": {
                "title": {"type": "text"},
                "body": {"type": "text"},
                "user_id": {
                    "type": "keyword"
                },
                "created": {
                    "type": "date"
                }
            }
        }
    }
}

_es.index(index="my_index", doc_type="test_type", id=1, body={"name": "python", "addr": "上海"})

_es.create(index="my_index", doc_type="test_type", id=1, ignore=409, body={"name": "python", "addr": "上海"})

result = _es.search(index="my_index",doc_type="test_type")
print(result)
result = _es.get(index="my_index", doc_type="test_type", id=1)
print(result)