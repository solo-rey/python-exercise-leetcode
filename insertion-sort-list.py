# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def isListAllSorted(self, head):
        current = head
        while current and current.next:
            if current.val > current.next.val:
                return False
            current = current.next
        return True

    def insertionSortList(self, head):
        if not head or not head.next or self.isListAllSorted(head):
            return head
        fakehead = ListNode(0)
        cur = head
        while cur:
            nextnode = cur.next
            pre = fakehead
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            cur = nextnode
        return fakehead.next

