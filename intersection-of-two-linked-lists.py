# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        nHeada,nHeadb = headA,headB
        lena = 0
        lenb = 0
        while nHeada != None:
            lena += 1
            nHeada = nHeada.next
        while nHeadb != None:
            lenb += 1
            nHeadb = nHeadb.next
        nHeada,nHeadb = headA,headB
        if lena >= lenb:
            for i in range(lena - lenb):
                nHeada = nHeada.next
            while nHeada != nHeadb:
                nHeada = nHeada.next
                nHeadb = nHeadb.next
                if not nHeada or not nHeadb:
                    return None
            return nHeada
        elif lenb > lena:
            for i in range(lenb - lena):
                nHeadb = nHeadb.next
            while nHeada != nHeadb:
                nHeada = nHeada.next
                nHeadb = nHeadb.next
                if not nHeada or not nHeadb:
                    return None
            return nHeadb

