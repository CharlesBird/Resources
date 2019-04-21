# 82. Remove Duplicates from Sorted List II
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        preNode = dummy_head
        while head and head.next:
            if head.val ==head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                preNode.next = head
            else:
                preNode = preNode.next
                head = head.next
        return dummy_head.next
