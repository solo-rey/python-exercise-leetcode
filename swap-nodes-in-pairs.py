# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return None
        if not head.next:
            return None
        l1 = head
        l2 = head.next
        head = l2
        l1.next = l2.next
        head.next = l1
        l3 = l1
        while l3.next:
            prev = l3
            l3 = l3.next
            l4 = l3.next
            if l4:
                l3.next = l4.next
                l4.next = l3
                prev.next = l4
        return head

    def swapPairs_better(self,head):
        if not head or not head.next:
            return head
        fakehead = ListNode(-1)
        fakehead.next = head
        p1 = fakehead
        p2 = fakehead.next
        while p2 and p2.next:
            nextnext = p2.next.next
            p2.next.next = p2
            p1.next = p2.next
            p2.next = nextnext
            p1 = p2
            p2 = p2.next
        return fakehead.next



