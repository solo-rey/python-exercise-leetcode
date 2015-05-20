# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        walker,runner = head,head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
        head1 = head
        head2 = walker.next
        walker.next = None
        head2 = self.reverse(head2)
        while head1 and head2:
            nextnode = head2.next
            head2.next = head1.next
            head1.next = head2
            head1 = head2.next
            head2 = nextnode



    def reverse(self,head):
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre

    def mergeTwoList(self,left,right):
        dummyhead = ListNode(-1)
        cur = dummyhead
        while left and right:
            if left:
                cur.next = left
                left = left.next
                cur = cur.next
            if right:
                cur.next = right
                right = right.next
                cur = cur.next
        return dummyhead.next

