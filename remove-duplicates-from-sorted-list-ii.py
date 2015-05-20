# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        dummyhead = ListNode(-1)
        dummyhead.next = head
        p0 = dummyhead
        p1 = p0.next
        p2 = p1.next
        flag = False
        while p2:
            if p1.val != p2.val:
                p0 = p1
                p1 = p2
                p2 = p2.next
            else:
                while p2 and p2.val == p1.val:
                    p2 = p2.next
                if p2 is None:
                    p0.next = None
                else:
                    p0.next = p2
                    p1 = p2
                    p2 = p2.next
        return dummyhead.next


    def deleteDuplicates_c(self,head):
        if head is None or head.next is None:
            return head
        dummyhead = ListNode(-1)
        dummyhead.next = head
        p0 = dummyhead
        p1 = p0.next
        p2 = p1.next
        flag = False
        while p2:
            if p1.val == p2.val:
                flag = True
                p2 = p2.next
                if p2 is None:
                    p0.next = None
            else:
                if flag:
                    p0.next = p2
                    flag = False
                else:
                    p0 = p1
                p1 = p2
                p2 = p2.next
        return dummyhead.next