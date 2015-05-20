# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        root = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            else:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
        if l1 is not None:
            dummy.next = l1
        if l2 is not None:
            dummy.next = l2
        return root.next
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head
        walker,runner = head,head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next

        head2 = walker.next
        walker.next= None
        head1 = head
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.mergeTwoLists(head1,head2)

