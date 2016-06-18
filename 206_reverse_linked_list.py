"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev,cur = head, head.next
        dummy = ListNode(-1)
        dummy.next = prev
        prev.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            dummy.next = cur
            prev = cur
            cur = next_node
        return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
s = Solution()
print s.reverseList(n1).val
