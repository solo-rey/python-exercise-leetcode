"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next and head.val != val:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        cur = dummy_head
        while cur and cur.next:
            if cur.next.val == val:
                next_node = cur.next.next
                cur.next = next_node
            else:
                cur = cur.next
        return dummy_head.next