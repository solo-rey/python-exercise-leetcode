# Definition for singly-linked list.
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

"""
take-away: create a dummy node, and attach the node with the new residual,carry, and a new node to the end if we have carry
"""

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current,carry = dummy,0
        while l1 != None or l2 != None:
            res = carry
            if l1 != None:
                res+=l1.val
                l1 = l1.next
            if l2 != None:
                res+=l2.val
                l2 = l2.next
            carry,res = res/10,res%10
            current.next = ListNode(res)
            current = current.next
        if carry == 1:
            current.next = ListNode(1)
        return dummy.next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current, carry = dummy, 0
    while l1 != None and l2 != None:
        result = carry
        if l1 != None:
            result += l1.val
        if l2 != None:
            result += l2.val
        carry, result = result / 10, result % 10
        current.next = ListNode(result)
        current = current.next
    if carry > 0:
        current.next = ListNode(carry)
    return dummy.next

