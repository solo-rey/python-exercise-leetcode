# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        start = ListNode(-1)
        end = ListNode(-1)

        start.next = head
        end.next = head
        dummy_head = start
        for i in range(n):
            end = end.next
        while end.next != None:
            end = end.next
            start = start.next
        start.next = start.next.next
        return dummy_head.next