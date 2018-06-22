from pymongo import MongoClient

client = MongoClient('118.190.149.30', 27017)
# 增加验证用户
db = client.test
db.authenticate('zhc', 'zhc123456')
# db.authenticate('other', 'other123456')
collection = db.user

# collection.insert({'name': 'Joy', 'age': 45, 'addr': '江苏'})

for item in collection.find():
    print(item)