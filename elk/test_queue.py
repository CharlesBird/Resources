from queue import Queue
import threading
from collections import deque

# q = Queue()
# thread_id = 1
#
#
# class Consume(threading.Thread):
#
#     def __init__(self, name=None):
#         global thread_id
#         threading.Thread.__init__(self, name=name)
#         self.name = name
#         self.q = q
#         self.Thread_id = thread_id
#         thread_id = thread_id + 1
#
#     def run(self):
#         while True:
#             try:
#                 task = self.q.get(block=True, timeout=1)
#             except Exception:
#                 print('Thread',  self.Thread_id, 'end')
#                 break
#             print("Starting ", self.Thread_id, self.name)
#
#             print(task)
#             self.q.task_done()
#             print("Ending ", self.Thread_id)
#
#
# class Productor(threading.Thread):
#
#     def __init__(self, name, m, n):
#         threading.Thread.__init__(self, name=name)
#         self.name = name
#         self.m = m
#         self.n = n
#         self.q = q
#
#     def run(self):
#         for i in range(self.m, self.n):
#             self.q.put(i)
#             print("Starting ", self.n, self.name)
#
#
# p1 = Productor('Productor1', 0, 10)
# p1.start()
# p2 = Productor('Productor2', 10, 20)
# p2.start()
# p3 = Productor('Productor3', 20, 30)
# p3.start()
# p1.join()
# p2.join()
# p3.join()
#
#
# worker1 = Consume('Consume1')
# worker1.start()
# worker2 = Consume('Consume2')
# worker2.start()
# worker3 = Consume('Consume3')
# worker3.start()
# q.join()
# print("Exiting Main Thread")
#
# d = deque()
# print(d)
# d.append(1)
# d.append(2)
# d.append(3)
# print(d.popleft())
# print(d.popleft())
# print(d)


q = Queue(maxsize=100)
# con = threading.Condition()
class ItemFilter(object):

    def __init__(self):
        self.d = deque()
        self.items = dict()

    def set_items(self, item):
        key = item['now_time']
        if key not in self.d:
            self.d.append(key)
        self.items.update({key: item})

def d2q(itemfilter):
    # print(self.d)
    while True:
        print(len(itemfilter.d))
        if len(itemfilter.d) == 1:
            break
        key = itemfilter.d.popleft()
        item = itemfilter.items.pop(key)
        q.put(item)
        if q.full():
            print('q is full')
            break


# class D2Q(threading.Thread):


def get_value():
    items = []
    while True:
        try:
            item = q.get(block=False)
            items.append(item)
        except Exception:
            print('Get error')
            break
    write_to_db(items)


def write_to_db(items):
    print(items)


items = [
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.11', 'diff': '-0.28', 'change_rate': '-0.36%', 'change_time': '2018-07-06 10:21:18', 'now_time': '2018-07-06 10:21:20', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.11', 'diff': '-0.28', 'change_rate': '-0.36%', 'change_time': '2018-07-06 10:21:18', 'now_time': '2018-07-06 10:21:21', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.11', 'diff': '-0.28', 'change_rate': '-0.36%', 'change_time': '2018-07-06 10:21:22', 'now_time': '2018-07-06 10:21:22', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.11', 'diff': '-0.28', 'change_rate': '-0.36%', 'change_time': '2018-07-06 10:21:22', 'now_time': '2018-07-06 10:21:22', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.11', 'diff': '-0.28', 'change_rate': '-0.36%', 'change_time': '2018-07-06 10:21:22', 'now_time': '2018-07-06 10:21:23', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:24', 'now_time': '2018-07-06 10:21:24', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:24', 'now_time': '2018-07-06 10:21:24', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:25', 'now_time': '2018-07-06 10:21:25', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:26', 'now_time': '2018-07-06 10:21:25', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:26', 'now_time': '2018-07-06 10:21:26', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:26', 'now_time': '2018-07-06 10:21:27', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:26', 'now_time': '2018-07-06 10:21:27', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:29', 'now_time': '2018-07-06 10:21:28', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:29', 'now_time': '2018-07-06 10:21:29', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:29', 'now_time': '2018-07-06 10:21:29', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:29', 'now_time': '2018-07-06 10:21:30', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
{'name': '伦敦布伦特原油期货 - 2018年9月 (LCOU8)', 'last_value': '77.12', 'diff': '-0.27', 'change_rate': '-0.35%', 'change_time': '2018-07-06 10:21:29', 'now_time': '2018-07-06 10:21:31', 'yesterday_close': '77.39', 'open_value': '77.56', 'today_low': '77.03', 'today_high': '77.67'},
]
itemfilter = ItemFilter()
for item in items:
    itemfilter.set_items(item)
# t1 = threading.Thread(target=d2q, args=(itemfilter,))
# t1.start()
# t2 = threading.Thread(target=get_value, args=())
# t2.start()
# t1.join()
# t2.join()
while True:
    d2q(itemfilter)
    get_value()






