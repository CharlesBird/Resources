# 返回一个可调用对象，该对象从其操作数中获取attr。如果请求多个属性，则返回一个属性元组。属性名也可以包含点。
from operator import attrgetter

from collections import namedtuple

User = namedtuple('User', ['name', 'age', 'addr'])
user = User('Charles', '28', 'shanghai')
name_user = attrgetter('name', 'age')
print(name_user(user))