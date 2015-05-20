# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head:
            return head
        dummyhead = ListNode(-1)
        dummyhead.next = head
        cnt = 0
        pre,cur = dummyhead,head
        while cur:
            cnt+=1
            next = cur.next
            if cnt == k:
                pre = self.reverse(pre,next)
                cnt = 0
            cur = next
        return dummyhead.next

    def reverse(self,pre,end):
        if not pre or not pre.next:
            return pre
        head = pre.next
        cur = pre.next.next
        while cur != end:
            head.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = head.next
        return head


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
s = Solution()
print s.reverseKGroup(l1,2)
