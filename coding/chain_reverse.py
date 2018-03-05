# 单链表逆序
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

# 第一种，循环反转单链表
# 使用pre指向前一个节点，curr指向当前节点，每次把cur->next指向pre
def nonrecurse(head):
    if head is None or head.next is None:
        return None
    pre = None
    cur = head
    h = head
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p = nonrecurse(head)
while p:
    print(p.value)
    p = p.next


# 递归实现单链表反转
def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
    if head is None:
        return None
    if head.next is None:
        newhead = head
    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head
        head.next = None
    return newhead

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
newhead = None
p = recurse(head, newhead)
while p:
    print(p.value)
    p = p.next

