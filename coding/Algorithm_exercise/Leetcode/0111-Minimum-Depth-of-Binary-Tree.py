"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         if root.left is None and root.right is None:
#             return 1
#         res = float('inf')
#         if root.left:
#             res = min(res, 1+self.minDepth(root.left))
#         if root.right:
#             res = min(res, 1+self.minDepth(root.right))
#         return res

# 迭代方式
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = float('inf')
        while stack:
            node, d = stack.pop()

            if node.left is None and node.right is None:
                res = min(res, d)
            else:
                if node.left:
                    stack.append((node.left, d+1))
                if node.right:
                    stack.append((node.right, d+1))
        return res