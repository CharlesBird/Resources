"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

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
#     def inorderTraversal(self, root: TreeNode):
#         res = []
#         self.rec_inorder(root, res)
#         return res
#
#     def rec_inorder(self, root, res):
#         if root:
#             self.rec_inorder(root.left, res)
#             res.append(root.val)
#             self.rec_inorder(root.right, res)


# 迭代方式
# class Solution:
#     def inorderTraversal(self, root: TreeNode):
#         stack, res = [], []
#         cur = root
#         while cur or stack:
#             if cur:
#                 stack.append(cur)
#                 cur = cur.left
#             else:
#                 cur = stack.pop()
#                 res.append(cur.val)
#                 cur = cur.right
#         return res

class Solution:
    def inorderTraversal(self, root: TreeNode):
        stack, res = [], []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res