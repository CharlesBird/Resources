from collections import deque

# 双端list

user_deque = deque(('Charles1', 'Charles2', 'Charles3', 'Charles4', 'Charles5'))
print(user_deque.count('Charles2'))
user_deque.appendleft('Charles0')
print(user_deque)
user_deque.popleft()
print(user_deque)
user_deque.insert(0, 'Charles0')
print(user_deque)
user_deque.extendleft(['Charles'])
print(user_deque)