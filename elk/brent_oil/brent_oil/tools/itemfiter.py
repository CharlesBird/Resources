from queue import Queue
from collections import deque
import logging
_logger = logging.getLogger(__name__)
q = Queue(maxsize=200)


class ItemFilter(object):

    def __init__(self):
        self.d = deque()
        self.items = dict()
        self.to_update_q = False

    def set_items(self, item):
        now_time = item['now_time']
        if now_time not in self.d:
            self.d.append(now_time)
        self.items.update({now_time: item})
        self.to_update_q = len(set([value['change_time'] for value in self.items.values()])) > 1 or len(self.items) > 200


def d2q(itemfilter):
    while True:
        if len(itemfilter.d) == 1:
            break
        key = itemfilter.d.popleft()
        item = itemfilter.items.pop(key)
        q.put(item)
        if q.full():
            _logger.warning('q is full')
            break


def get_items():
    items = []
    while True:
        try:
            item = q.get(block=False)
            items.append(item)
        except Exception as e:
            _logger.warning('q is empty')
            break
    return items
