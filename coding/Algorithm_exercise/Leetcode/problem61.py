# 61. Rotate List
"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or not k:
            return head
        L = 0
        first = head
        while first:
            L += 1
            first = first.next
        right_L = k % L
        left_L = L - right_L
        left_head = head
        while left_L > 1:
            left_L -= 1
            head = head.next
        new_head = head.next
        if new_head is None:
            return left_head
        right_end = new_head
        head.next = None
        while right_L > 1:
            right_L -= 1
            right_end = right_end.next
        right_end.next = left_head
        return new_head
