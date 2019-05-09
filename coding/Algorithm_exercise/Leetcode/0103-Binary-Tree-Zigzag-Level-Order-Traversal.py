"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        res, level = [], [root]
        rev = False
        while root and level:
            if not rev:
                res.append([node.val for node in level])
                rev = True
            else:
                res.append([node.val for node in level][::-1])
                rev = False
            childNodes = [(node.left, node.right) for node in level]
            level = [leaf for leafNodes in childNodes for leaf in leafNodes if leaf]
        return res