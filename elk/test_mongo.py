from pymongo import MongoClient

client = MongoClient('118.190.149.30', 27017)
# 增加验证用户
db_auth = client.admin
db_auth.authenticate('test_user', '123456')
db = client.test
collection = db.user

collection.insert({'name': 'Emily', 'age': 17, 'addr': '北京'})

for item in collection.find():
    print(item)