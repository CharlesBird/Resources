"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#
#         res = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#         return res

# 迭代方式
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [(root, 1)]
        res = 0
        while stack:
            node, d = stack.pop()

            if node:
                if node.left is None and node.right is None:
                    res = max(res, d)
                else:
                    if node.left:
                        stack.append((node.left, d+1))
                    if node.right:
                        stack.append((node.right, d+1))
        return res