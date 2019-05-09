# 92. Reverse Linked List II
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None:
            return head
        cur, preNode = head, None
        while m > 1:
            preNode = cur
            cur = cur.next
            m -= 1
            n -= 1
        left, right = preNode, cur

        while n:
            nextNode = cur.next
            cur.next = preNode
            preNode = cur
            cur = nextNode
            n -= 1
        if left:
            left.next = preNode
        else:
            head = preNode
        right.next = cur
        return head

        # Method Two
        # if not head:
        #     return None
        #
        # left, right = head, head
        # stop = False
        #
        # def recurseAndReverse(right, m, n):
        #     nonlocal left, stop
        #
        #     if n == 1:
        #         return
        #
        #     right = right.next
        #
        #     if m > 1:
        #         left = left.next
        #
        #     recurseAndReverse(right, m - 1, n - 1)
        #
        #     if left == right or right.next == left:
        #         stop = True
        #
        #     if not stop:
        #         left.val, right.val = right.val, left.val
        #         left = left.next
        #
        # recurseAndReverse(right, m, n)
        # return head

