"""python实现链表"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.pnext = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def size(self):
        """链表大小"""
        count = 0
        if self.head is not None:
            current_node = self.head
            while current_node is not None:
                count += 1
                current_node = current_node.pnext
        return count

    def is_empty(self):
        """链表是否为空"""
        if self.head is None or self.size() == 0:
            return True
        return False

    def append(self, data):
        """给链表添加元素，默认添加在尾部"""
        this_node = Node(data)
        if self.is_empty():
            self.head = this_node
        else:
            node = self.head
            while node.pnext:
                node = node.pnext
            node.pnext = this_node
        return self.head

    def prepend(self, data):
        """给链表头部添加元素"""
        new_head = Node(data)
        if self.is_empty():
            self.head = new_head
        else:
            new_head.pnext = self.head
            self.head = new_head
        return self.head

    def insert(self, index, data):
        """列表的插入"""
        if not isinstance(index, int):
            raise Exception("Index must be Integer")
        if self.is_empty():
            raise Exception("It's a empty list")
        if index <= 0 or index > self.size():
            raise Exception("Index value is out of range")
        else:
            if index == 1:
                self.prepend(data)
            else:
                this_node = Node(data)
                pre_node = self.head
                current_node = self.head.next
                while index > 2:
                    pre_node = current_node
                    current_node = pre_node.pnext
                    index -= 1
                pre_node.pnext = this_node
                this_node.pnext = current_node
        return None

    def delete(self, index):
        """链表指定位置删除"""
        if not isinstance(index, int):
            raise Exception("Index must be Integer")
        if index <= 0 or index > self.size():
            raise Exception("Index value is out of range")
        elif index == 1:
            self.head = self.head.pnext
        else:
            pre_node = self.head
            current_node = pre_node.pnext
            while index > 2:
                pre_node = current_node
                current_node = current_node.pnext
                index -= 1
            pre_node.pnext = current_node.pnext
        return None

    def update(self, index, data):
        """链表指定位置更新"""
        if not isinstance(index, int):
            raise Exception("Index must be Integer")
        if index <= 0 or index > self.size():
            raise Exception("Index value is out of range")
        elif index == 1:
            this_node = Node(data)
            this_node.pnext = self.head.pnext
            self.head = this_node
        else:
            current_node = self.head
            while index > 1:
                current_node = current_node.pnext
                index -= 1
            current_node.data = data
        return None

    def get_value(self, index):
        """指定位置获取列表的值"""
        if not isinstance(index, int):
            raise Exception("Index must be Integer")
        if index <= 0 or index > self.size():
            raise Exception("Index value is out of range")
        if index == 1:
            return self.head.data
        else:
            current_node = self.head
            while index > 1:
                current_node = current_node.pnext
                index -= 1
            return current_node.data

    def peek(self):
        """获取列表尾部值，不删除节点"""
        return self.get_value(self.size())

    def pop(self):
        """获取列表尾部值，并删除节点"""
        if self.head is None or self.size() == 0:
            raise Exception("List is Null")
        if self.size() == 1:
            top = self.head.data
            self.head = None
            return top
        else:
            pre_node = self.head
            current_node = pre_node.pnext
            while current_node.pnext is not None:
                pre_node = current_node
                current_node = current_node.pnext
            top = current_node.data
            current_node = None
            pre_node.pnext = None
            return top

    def clear(self):
        """清除所有节点"""
        self.head = None
        return self.head

    def reverse(self):
        """单链表逆序"""
        if self.head is None or self.size() == 0:
            return None
        if self.size() == 1:
            return None
        else:
            pre = None
            current_node = self.head
            while current_node is not None:
                tmp = current_node.pnext
                current_node.pnext = pre
                pre = current_node
                current_node = tmp
            self.head = pre
        return None

    def print_linked_list(self):
        """打印所有节点值"""
        if self.is_empty():
            return None
        else:
            current_node = self.head
            result = 'head --> %s' % current_node.data
            while current_node.pnext is not None:
                current_node = current_node.pnext
                result += ' --> %s' % current_node.data
            return result


if __name__ == '__main__':
    ll = LinkedList()

    ll.append('q')
    ll.append('w')
    ll.append('e')
    ll.prepend('m')
    ll.reverse()

    ll.insert(1, 'g')
    print(ll.print_linked_list())
    ll.delete(4)
    ll.update(3, 'f')
    print(ll.get_value(3))
    print(ll.peek())
    print(ll.pop())
    print(ll.print_linked_list())
    ll.clear()
    print(ll.size(), ll.is_empty(), ll.print_linked_list())