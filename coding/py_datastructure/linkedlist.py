"""python实现链表"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.pnext = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.lenth = 0

    def is_empty(self):
        return self.lenth

    def append(self, n):
        if isinstance(n, Node):
            raise Exception("This not a Node")
        else:
            this_node = Node(n)
        if self.is_empty():
            self.head = this_node
        else:
            node = self.head
            while node.pnext:
                node = node.pnext
            node.pnext = this_node
        self.lenth += 1