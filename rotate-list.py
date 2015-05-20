# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        length = 1
        fakehead = ListNode(-1)
        fakehead.next = head
        p1 = head
        p2 = head
        while p2.next != None:
            length+=1
            p2 = p2.next
        k = k%length
        if k == 0 :
            return head
        p2 = head
        for i in range(k):
            p2 = p2.next
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = fakehead.next
        fakehead.next = p1.next
        p1.next = None
        return fakehead.next

l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
sol = Solution()
print sol.rotateRight(l1,1).val
