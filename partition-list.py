class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


# @param head, a ListNode
# @param x, an integer
# @return a ListNode
def partition(head, x):
    """two new lists, one small,one big, and link together"""
    if not head or not head.next:
        return head
    smallhead = ListNode(-1)
    bighead = ListNode(-1)
    newsmall = smallhead
    newbig = bighead
    t = head
    while t:
        if t.val >= x:
            bighead.next = t
            bighead = bighead.next
        else:
            smallhead.next = t
            smallhead = smallhead.next
        t = t.next
    smallhead.next = newbig.next
    bighead.next = None
    return newsmall.next

l1 = ListNode(1)
l2 = ListNode(1)
l1.next = l2
print partition(l1,0)
