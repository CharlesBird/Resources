from collections import defaultdict

user_list = ('Charles1', 'Charles2', 'Charles1', 'Charles2', 'Charles1')

user_dict = defaultdict(int)
for user in user_list:
    user_dict[user] += 1

print(user_dict)


default_v = {
    'group1':
        {'name': '',
         'num': 0}
}

def default_group():
    return default_v

group_dict = defaultdict(default_group)
# group_dict['user']
print(group_dict, group_dict['user'])
