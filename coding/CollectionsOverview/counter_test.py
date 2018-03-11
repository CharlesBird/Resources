from collections import Counter

user_list = ('Charles1', 'Charles2', 'Charles1', 'Charles2', 'Charles1')
c = Counter(user_list)
print(c)
new_c = Counter('esiseinjegrnnsudawiwewnefreirak')
print(new_c)
# new_c.update('eignernfqiwjqioefw')
new_c2 = Counter('eignernfqiwjqioefw')
new_c.update(new_c2)
print(new_c)
top_n = new_c.most_common(4)
print(top_n)