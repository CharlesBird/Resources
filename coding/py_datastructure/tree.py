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
        """添加元素"""
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while q:
                current_node = q.pop(0)
                if current_node.lnode is None:
                    current_node.lnode = node
                    return None
                elif current_node.rnode is None:
                    current_node.rnode = node
                    return None
                else:
                    q.append(current_node.lnode)
                    q.append(current_node.rnode)

    def level_order(self):
        """层次遍历"""
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

    def pre_order(self, root, res=[]):
        """前序遍历"""
        if root is not None:
            res.append(root.value)
            self.pre_order(root.lnode)
            self.pre_order(root.rnode)
        return res

    def mid_order(self, root, res=[]):
        """中序遍历"""
        if root is not None:
            self.mid_order(root.lnode)
            # print(root.value)
            res.append(root.value)
            self.mid_order(root.rnode)
        return res

    def post_order(self, root, res=[]):
        """后序遍历"""
        if root is not None:
            self.post_order(root.lnode)
            self.post_order(root.rnode)
            res.append(root.value)
        return res

    def get_size(self):
        """二叉树节点数量"""
        size = 0
        if self.root:
            q = [self.root]
            while q:
                current_node = q.pop(0)
                size += 1
                if current_node.lnode:
                    q.append(current_node.lnode)
                if current_node.rnode:
                    q.append(current_node.rnode)
        return size

    def height(self, root):
        """二叉树最大高度"""
        if root is None:
            return 0
        else:
            ldeepth = self.height(root.lnode)
            rdeepth = self.height(root.rnode)
        return max(ldeepth+1, rdeepth+1)

    def deepth(self, root):
        """二叉树最大深度"""
        return self.height(root) - 1

if __name__ == '__main__':
    t = BTree()
    for i in range(10):
        t.add(i)
    print('层次遍历：', t.level_order())
    print('前序遍历：', t.pre_order(t.root))
    print('中序遍历：', t.mid_order(t.root))
    print('后序遍历：', t.post_order(t.root))
    print('节点数量：', t.get_size())
    print('最大高度：', t.height(t.root))
    print('最大深度：', t.deepth(t.root))


