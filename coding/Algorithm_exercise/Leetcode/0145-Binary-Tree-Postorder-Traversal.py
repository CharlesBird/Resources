"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        self.rec_postorder(root, res)
        return res

    def rec_postorder(self, root, res):
        if root:
            self.rec_postorder(root.left, res)
            self.rec_postorder(root.right, res)
            res.append(root.val)

# 迭代方式
class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        while output:
            res.append(output.pop().val)
        return res
