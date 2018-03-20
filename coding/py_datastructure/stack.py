"""
python数据结构栈的实现
第一种通过节点指针实现
第二种通过python自身list类实现
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    """第一种实现方法"""
    def __init__(self):
        self.top = None

    def push(self, value):
        n = Node(value)
        n.next = self.top
        self.top = n
        return n.value

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            return None

    def pop(self):
        if self.top is None:
            return None
        else:
            tem = self.top.value
            self.top = self.top.next
            return tem

    def is_empty(self):
        if self.top is not None:
            return False
        else:
            return True

    def size(self):
        lenth = 0
        if self.top:
            lenth += 1
            n = self.top.next
            while n:
                lenth += 1
                n = n.next
        return lenth


class Stack2(object):
    """第二种实现方法"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)
        return value

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def foo1():
    s = Stack()
    for i in range(1000):
        s.push(i)
    for _ in range(1000):
        s.peek()
        s.pop()


def foo2():
    s = Stack2()
    for i in range(1000):
        s.push(i)
    for _ in range(1000):
        s.peek()
        s.pop()


if __name__ == '__main__':
    import timeit

    t1 = timeit.Timer(foo1)
    t2 = timeit.Timer(foo2)
    print(t1.repeat(3, 10000), t2.repeat(3, 10000))



    # s = Stack()
    # print('before push is_empty', s.is_empty())
    # print('before push size', s.size())
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # print('after push is_empty', s.is_empty())
    # print('after push size', s.size())
    # print('peek', s.peek())
    # print('pop', s.pop())
    # print('after one pop size', s.size())
    # print('peek', s.peek())
    # print('pop', s.pop())
    # print('peek', s.peek())
    # print('pop', s.pop())
    # print('is_empty', s.is_empty())
    # print('after pop size', s.size())
