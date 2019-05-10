"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        new_ls = []
        for head in lists:
            while head:
                new_ls.append(head.val)
                head = head.next
        new_ls.sort()
        head = curr = ListNode(0)
        for i in new_ls:
            curr.next = ListNode(i)
            curr = curr.next
        return head.next