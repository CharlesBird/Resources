"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3



But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3



Note:
Bonus points if you could solve it both recursively and iteratively.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)


# DFS，深度优先搜索
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            else:
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
        return True


# BFS，广度优先搜索
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        q1, q2 = [root], [root]
        while q1 and q2:
            node1, node2 = q1.pop(0), q2.pop(0)
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.right)
            q2.append(node2.left)
        return not q1 and not q2

        # q = [(root, root)]
        # while q:
        #     node1, node2 = q.pop(0)
        #     if not node1 and not node2:
        #         continue
        #     if not node1 or not node2:
        #         return False
        #     if node1.val != node2.val:
        #         return False
        #     else:
        #         q.append((node1.left, node2.right))
        #         q.append((node1.right, node2.left))
        # return True