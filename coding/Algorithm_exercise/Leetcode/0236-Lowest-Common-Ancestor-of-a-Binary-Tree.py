"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.



Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 在root中寻找p和q
    # 如果p和q都在root所在的二叉树中, 则返回LCA
    # 如果p和q只有一个在root所在的二叉树中, 则返回p或者q
    # 如果p和q均不在root所在的二叉树中, 则返回NULL
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == q or root == p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right


class Solution2:
    # 在root中寻找p和q, 如果包含则返回 true
    # 否则返回false
    # root是p或者q；root的左子树包含p或q；root的右子树包含p或q；三个条件有两个满足
    # 则 ret = root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ret = None
        self.dfs(root, p, q)
        return self.ret

    def dfs(self, root, p, q):
        if not root:
            return False
        mid = False
        if root == q or root == p:
            mid = True

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if mid + left + right >= 2:
            self.ret = root
        return mid or left or right