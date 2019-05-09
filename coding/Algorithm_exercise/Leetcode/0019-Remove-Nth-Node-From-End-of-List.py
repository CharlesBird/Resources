"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        L = 0
        first = head
        while first:
            L += 1
            first = first.next
        Ind = L - n
        curr = dummy_head
        while Ind:
            curr = curr.next
            Ind -= 1
        curr.next = curr.next.next
        return dummy_head.next