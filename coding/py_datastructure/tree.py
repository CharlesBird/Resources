"""python 实现树结构"""


class Node(object):
    """构造树节点，包括树值，左右节点"""

    def __init__(self, value):
        self.value = value
        self.lnode = None
        self.rnode = None


class BTree(object):
    """实现树结构，包括树层次遍历，前序遍历，中序遍历，后序遍历"""

    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while q:

                current_node = q.pop(0)
                print(current_node.value)
            if current_node.lnode is None:
                print('111111')
                current_node.lnode = node
                return None
            elif current_node.rnode is None:
                print('222222')
                current_node.rnode = node
                return None
            else:
                print('33333')
                q.append(current_node.lnode)
                q.append(current_node.rnode)

    def level_order(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.value]
        while q:
            current_node = q.pop(0)
            if current_node.lnode is not None:
                q.append(current_node.lnode)
                res.append(current_node.lnode.value)
            if current_node.rnode is not None:
                q.append(current_node.rnode)
                res.append(current_node.rnode.value)
        return res


if __name__ == '__main__':
    t = BTree()
    t.add(0)
    t.add(1)
    t.add(2)
    # t.add(3)
    # t.add(4)
    # t.add(5)
    print(t.level_order())


