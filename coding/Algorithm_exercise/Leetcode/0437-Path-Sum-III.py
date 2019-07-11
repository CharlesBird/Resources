"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def findPath(self, node, s):
        if not node:
            return 0
        res = 0
        if node.val == s:
            res += 1
        res += self.findPath(node.left, s - node.val)
        res += self.findPath(node.right, s - node.val)
        return res


class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        import collections
        self.res = 0
        d = collections.defaultdict(int)
        d[0] = 1
        if root:
            self.dfs(root, d, root.val, sum)
        return self.res

    def dfs(self, root, d, curSum, s):
        self.res += d[curSum-s]
        d[curSum] += 1
        if root.left:
            self.dfs(root.left, d, curSum+root.left.val, s)
        if root.right:
            self.dfs(root.right, d, curSum + root.right.val, s)
        d[curSum] -= 1