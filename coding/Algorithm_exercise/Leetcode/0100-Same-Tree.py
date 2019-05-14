"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# DFS，深度优先搜索
class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            pNode, qNode = stack.pop()

            if not pNode and not qNode:
                continue
            if not pNode or not qNode:
                return False
            else:
                if pNode.val != qNode.val:
                    return False
                stack.append((pNode.right, qNode.right))
                stack.append((pNode.left, qNode.left))
        return True


# BFS，广度优先搜索
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        q = [(p, q)]
        while q:
            pNode, qNode = q.pop(0)

            if not pNode and not qNode:
                continue
            if not pNode or not qNode:
                return False
            else:
                if pNode.val != qNode.val:
                    return False
                q.append((pNode.right, qNode.right))
                q.append((pNode.left, qNode.left))
        return True