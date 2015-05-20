# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
#
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:
            return None
        nodes = []
        p = head
        while p:
            nodes.append(p.val)
            p = p.next
        return self.helper(nodes,0,len(nodes)-1)

    def helper(self,nodes,start,end):
        if start > end:
            return None
        mid = (start+end) / 2
        root = TreeNode(nodes[mid])
        root.left = self.helper(nodes,start,mid-1)
        root.right = self.helper(nodes,mid+1,end)
        return root