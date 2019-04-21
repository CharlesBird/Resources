# 21. Merge Two Sorted Lists
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val <= l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
            curNode = head
            while l1 and l2:
                if l1.val <= l2.val:
                    curNode.next = l1
                    curNode = curNode.next
                    l1 = l1.next
                else:
                    curNode.next = l2
                    curNode = curNode.next
                    l2 = l2.next
            while l1:
                curNode.next = l1
                curNode = curNode.next
                l1 = l1.next
            while l2:
                curNode.next = l2
                curNode = curNode.next
                l2 = l2.next
        return head


        # Method Two
        # l1_list = []
        # while l1:
        #     l1_list.append(l1.val)
        #     l1 = l1.next
        # l2_list = []
        # while l2:
        #     l2_list.append(l2.val)
        #     l2 = l2.next
        # head = dummy_head = ListNode(0)
        # for v in sorted(l1_list+l2_list):
        #     head.next = ListNode(v)
        #     head = head.next
        # return dummy_head.next