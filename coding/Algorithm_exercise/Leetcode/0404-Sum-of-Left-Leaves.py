"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, node, leftsum):
        if not node:
            return 0
        if node.left and not node.left.left and not node.left.right:
            leftsum += node.left.val
        if node.left:
            leftsum = self.dfs(node.left, leftsum)
        if node.right:
            leftsum = self.dfs(node.right, leftsum)
        return leftsum


class Solution2:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)