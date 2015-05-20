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

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if lists is None:
            return None
        p = lists[0]
        for idx in range(1,len(lists)):
            p = mergeTwoLists(p,lists[idx])
        return p