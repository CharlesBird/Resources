# 24. Swap Nodes in Pairs
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node1, node2 = head, head.next
        nextNode = node2.next
        head = node2
        node2.next = node1
        node1.next = self.swapPairs(nextNode)
        return head

        # Method Two
        # dummy_head = ListNode(0)
        # dummy_head.next = head
        # p = dummy_head
        # while p.next and p.next.next:
        #     node1 = p.next
        #     node2 = p.next.next
        #     nextNode = node2.next
        #     node2.next = node1
        #     node1.next = nextNode
        #     p.next = node2
        #
        #     p = node1
        # return dummy_head.next
