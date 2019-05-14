"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_left = self.leftHight(root.left)
        left_right = self.rightHight(root.left)
        if left_left == left_right:
            return 1 + ((1 << left_left) - 1) + self.countNodes(root.right)
        return 1 + ((1 << left_right) - 1) + self.countNodes(root.left)

    def leftHight(self, root):
        if not root:
            return 0
        return 1 + self.leftHight(root.left)

    def rightHight(self, root):
        if not root:
            return 0
        return 1 + self.rightHight(root.right)


class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.getHight(root.left)
        right_height = self.getHight(root.right)
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        return (1 << right_height) + self.countNodes(root.left)

    def getHight(self, root):
        if not root:
            return 0
        return 1 + self.getHight(root.left)