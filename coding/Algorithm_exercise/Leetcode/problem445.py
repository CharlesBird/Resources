# 445. Add Two Numbers II
"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy_head = ListNode(0)
        s1 = ''
        s2 = ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        s = str(int(s1) + int(s2))
        for i in range(len(s)):
            head.next = ListNode(s[i])
        return dummy_head.next

        # Method Two
        # dummy_head = ListNode(0)
        # l1_size = l2_size = 1
        # nextNode1, nextNode2 = l1.next, l2.next
        # while nextNode1:
        #     l1_size += 1
        #     nextNode1 = nextNode1.next
        #
        # while nextNode2:
        #     l2_size += 1
        #     nextNode2 = nextNode2.next
        #
        # k = 0
        # while l1_size or l2_size or k:
        #     v1 = v2 = 0
        #     if l1_size:
        #         currNode1 = l1
        #         for _ in range(l1_size - 1):
        #             currNode1 = currNode1.next
        #         v1 = currNode1.val
        #     if l2_size:
        #         currNode2 = l2
        #         for _ in range(l2_size - 1):
        #             currNode2 = currNode2.next
        #         v2 = currNode2.val
        #     k, v = divmod(v1 + v2 + k, 10)
        #
        #     curr = ListNode(v)
        #     curr.next = dummy_head.next
        #     dummy_head.next = curr
        #     l1_size = l1_size and l1_size - 1
        #     l2_size = l2_size and l2_size - 1
        # return dummy_head.next
