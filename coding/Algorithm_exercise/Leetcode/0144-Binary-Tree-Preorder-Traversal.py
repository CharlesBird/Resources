"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
# class Solution:
#     def preorderTraversal(self, root: TreeNode):
#         res = []
#         self.rec_preorder(root, res)
#         return res
#
#     def rec_preorder(self, root, res):
#         if root:
#             res.append(root.val)
#             self.rec_preorder(root.left, res)
#             self.rec_preorder(root.right, res)

# 迭代方式
class Solution:
    def preorderTraversal(self, root: TreeNode):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res