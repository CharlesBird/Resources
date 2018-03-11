from collections import namedtuple

User = namedtuple('User', ['name', 'age', 'addr'])
user = User('Charles', '28', 'shanghai')
print(user.name, user.age, user.addr)
u = user._asdict()
print(u, u['name'])
user2 = user._make(('Charles2', '28', 'shanghai'))
print(user2.name, user2.age, user2.addr)
d = {'name': 'Charles3', 'age': 19, 'addr': 'beijing'}
user3 = User(**d)
print(user3.name, user3.age, user3.addr)