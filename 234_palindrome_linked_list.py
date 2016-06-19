"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Another way could be reverse linked-list if required O(1) space
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        fast, slow = head, head
        s = []
        s.append(head)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            s.append(slow)
        # odd numbers of node
        if not fast.next:
            s.pop()
        while slow.next:
            slow = slow.next
            t = s.pop()
            if t.val != slow.val:
                return False
        return len(s) == 0


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
print s.isPalindrome(n1)