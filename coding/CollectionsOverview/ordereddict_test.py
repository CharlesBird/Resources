from collections import OrderedDict

user_dict = OrderedDict()
user_dict['a'] = 'Charles1'
user_dict['c'] = 'Charles2'
user_dict['b'] = 'Charles3'
print(user_dict)

u = user_dict.popitem()
print(u)
print(user_dict)

user_dict.move_to_end('a')
print(user_dict)