"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        def helper(node, include):
            if not node:
                return 0

            res = helper(node.left, True) + helper(node.right, True)
            if include:
                res = max(node.val + helper(node.left, False) + helper(node.right, False), res)

            return res

        return helper(root, True)


class Solution2:
    def rob(self, root: TreeNode) -> int:
        # Time Complexity: O(n), where n is the nodes' number in the tree
        # Space Complexity: O(1)
        def helper(node):
            if not node:
                return 0, 0

            resultL = helper(node.left)
            resultR = helper(node.right)

            print(resultL[1] + resultR[1], max(resultL[1] + resultR[1], node.val + resultL[0] + resultR[0]))

            return resultL[1] + resultR[1], max(resultL[1] + resultR[1], node.val + resultL[0] + resultR[0])

        return max(helper(root))

[3,2,3,None,3,None,1]
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
Solution2().rob(root)