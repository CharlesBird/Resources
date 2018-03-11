from collections import ChainMap

user_dict1 = {'a': 'Charles1', 'b': 'Charles2'}
user_dict2 = {'c': 'Charles3', 'd': 'Charles4'}
user_dict3 = {'b': 'Charles3', 'f': 'Charles4'}
new_dict = ChainMap(user_dict1, user_dict2, user_dict3)
print(new_dict.maps)
new_dict.maps[0]['b'] = 'Jeff'
for k, v in new_dict.items():
    print(k, v)