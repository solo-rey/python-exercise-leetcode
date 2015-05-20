# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        pre,cur = head,head.next
        while cur:
            tmp = cur.next
            if pre.val == cur.val:
                pre.next = tmp
                cur = tmp
            else:
                pre = pre.next
                cur = cur.next
        return head
