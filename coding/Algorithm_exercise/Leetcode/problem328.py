# update_timestamps
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Method One
        if head is None:
            return None
        odd = head
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

        # Method Two
        # odd = odd_head = ListNode(0)
        # even = even_head = ListNode(0)
        # i = 0
        # while head:
        #     i += 1
        #     if i % 2 == 1:
        #         odd.next = head
        #         odd = odd.next
        #     else:
        #         even.next = head
        #         even = even.next
        #     head = head.next
        # even.next = None
        # odd.next = reven_head.next
        # return odd_head.next