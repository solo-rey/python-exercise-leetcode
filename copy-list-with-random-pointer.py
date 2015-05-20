# Definition for singly-linked list with a random pointer.
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        p,num = head,0
        while p:
            t = RandomListNode(p.label)
            t.next,p.next,t.random = p.next,t,p.random
            p,num = t.next,num+1
        p = head.next
        for i in range(num):
            if p.random:
                p.random = p.random.next
            if p and p.next:
                p = p.next.next
        p1,p2,newHead = head,head.next,head.next
        for i in range(num-1):
            p1.next,p2.next = p1.next.next,p2.next.next
            p1,p2 = p1.next,p2.next
        return newHead