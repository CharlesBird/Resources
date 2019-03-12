# 返回一个可调用对象，该对象使用操作数的getItem方法从其操作数中提取项。如果指定了多个项，则返回查找值的元组
from operator import itemgetter

print(itemgetter(1)('ABCDEF'))

print(itemgetter(1,3,5)('ABCDEF'))

print(itemgetter(slice(2,None))('ABCDEF'))

d = {'name': 'Charles', 'age': 18, 'addr': 'Shanghai'}

print(itemgetter('name')(d))

# 获取类中字段的值
class User:
    def __init__(self, seq=None, **kwargs):
        self.d = {}

    def __iter__(self):
        pass

    def __getitem__(self, item):
        return self.d[item]

    def __setitem__(self, key, value):
        self.d[key] = value

user = User()
user['name'] = 'Zhangsan'
user['age'] = '18'
user['addr'] = 'shanghai'
print(itemgetter('name')(user))

# 排序
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = itemgetter(1)
print(list(map(getcount, inventory)))
print(sorted(inventory, key=getcount))