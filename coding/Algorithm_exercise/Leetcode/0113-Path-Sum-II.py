"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res = []
        if not root:
            return res
        tres = []
        self.dfs(root, tres, sum, res)

        return res

    def dfs(self, root, tres, s, res):
        tr = tres[:]
        tr.append(root.val)
        if not root.left and not root.right:
            if sum(tr) == s:
                res.append(tr)
            return

        if root.left:
            self.dfs(root.left, tr, s, res)
        if root.right:
            self.dfs(root.right, tr, s, res)