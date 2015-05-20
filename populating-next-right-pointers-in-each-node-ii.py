# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        p = root.next
        while p:
            if p.left:
                p=p.left
                break
            if p.right:
                p=p.right
                break
            p=p.next
        if root.right:
            root.right.next=p
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = p
        self.connect(root.right)
        self.connect(root.left)