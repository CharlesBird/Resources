# 234. Palindrome Linked List
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        preNode = None
        while slow:
            nextNode = slow.next
            slow.next = preNode
            preNode = slow
            slow = nextNode
        while preNode:
            if head.val != preNode.val:
                return False
            head, preNode = head.next, preNode.next
        return True