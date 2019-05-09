"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        res, level = [], [root]
        while root and level:
            res.append(level[-1].val)
            # childs = [(node.left, node.right) for node in level]
            level = [leaf for child in [(node.left, node.right) for node in level] for leaf in child if leaf]
        return res