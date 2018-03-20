"""python实现队列"""


class Queue(object):

    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full.")
        self.queue.append(value)
        return value

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty.")
        firstEle = self.queue[0]
        self.queue.remove(firstEle)
        return firstEle

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self):
        if len(self.queue) == self.size:
            return True
        return False

    def size(self):
        return len(self.queue)

    def clearall(self):
        lists = []
        for _ in range(self.getsize()):
            lists.append(self.dequeue())
        return lists

    def getsize(self):
        return len(self.queue)


if __name__ == '__main__':
    q = Queue(10)
    for i in range(8):
        q.enqueue(i)
    print(q.dequeue())
    print(q.getsize())
    print(q.clearall())