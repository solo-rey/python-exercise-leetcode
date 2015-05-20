class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


# @param head, a ListNode
# @return a list node
def detectCycle(self, head):
    if not head or not head.next:
        return None
    slow = head
    fast = head
    while True:
        if not fast or not fast.next:
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = head
    if slow != fast:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        return slow.next
    else:
        return slow



