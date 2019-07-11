"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

         _______6______
      /                \
  ___2__              ___8__
 /      \           /      \
0       4          7        9
       / \
      3   5

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

BST，所以对于一个树和两个目标节点，有三种情况：
1 两个目标节点值都小于树的根节点的值，这种情况下所求LCA肯定在树的左子树上；
2 两个目标节点值都大于树的根节点的值，这种情况下所求LCA肯定在树的右子树上；
3 两个目标节点中要么有一个节点值和树的根节点值相等，要么一个大于一个小于树的根节点值，这些情况下LCA就是树的根节点了。

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        curNode = root
        while curNode:
            if p_val > curNode.val and q_val > curNode.val:
                curNode = curNode.right
            elif p_val < curNode.val and q_val < curNode.val:
                curNode = curNode.left
            else:
                return curNode