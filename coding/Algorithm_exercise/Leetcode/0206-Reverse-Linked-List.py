"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None  # 声明前节点
        cur = head  # 声明当前节点
        while cur is not None:
            nextNode = cur.next  # 声明下一个节点
            cur.next = preNode  # 当前节点指向前节点
            preNode = cur  # 前节点指向当前节点
            cur = nextNode  # 前节点指向当前下一个节点
        head = preNode
        return head