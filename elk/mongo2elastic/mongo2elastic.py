from pymongo import MongoClient
import jieba

client = MongoClient('118.190.149.30', 27017)
# 增加验证用户
db = client.topchinaz
db.authenticate('zhc', 'zhc123456')
# db.authenticate('other', 'other123456')
collection = db.allranking

n = collection.count()
print(n)

for item in collection.find():
    if item.get('registered_capital'):
        cut = jieba.cut(item.get('registered_capital'))
        lt = list(cut)
        if '人民币' in lt:
            print(lt, item)