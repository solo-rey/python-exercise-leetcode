# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        stk = []
        stk.append(root)
        pre = None
        while len(stk) > 0:
            node = stk.pop()
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
            if pre:
                pre.left = None
                pre.right = node
            pre = node
