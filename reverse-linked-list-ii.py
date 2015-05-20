"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ? m ? n ? length of list.
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# @param head, a ListNode
# @param m, an integer
# @param n, an integer
# @return a ListNode
"""
http://www.cnblogs.com/4everlove/p/3651002.html
"""
def reverseBetween(head, m, n):
    if not head:
        return head
    dummyhead = ListNode(-1)
    dummyhead.next = head
    prev = dummyhead
    cur = prev.next
    p1 = cur.next
    p2 = head
    for i in range(1,m):
        prev = cur
        cur = cur.next
    if cur:
        p1 = cur.next

    if p1:
        p2 = p1.next
    for i in range(m,n):
        p1.next = cur
        cur = p1
        p1 = p2
        if p2:
            p2 = p2.next
    prev.next.next = p1
    prev.next = cur
    return dummyhead.next

