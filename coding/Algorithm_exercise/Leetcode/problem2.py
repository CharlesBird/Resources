# 2. Add Two Numbers
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy_head = ListNode(0)
        k = 0
        while l1 or l2 or k:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            s = v1 + v2
            v = s % 10 + k
            if v >= 10:
                s = v
                v = v % 10
            head.next = ListNode(v)
            head = head.next
            k = s // 10
        return dummy_head.next

l1 = None
l2 = None
for i in [5]:
    l1 = ListNode(i)
    l2 = ListNode(i)
Solution().addTwoNumbers(l1, l2)