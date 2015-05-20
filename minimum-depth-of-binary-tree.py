class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        """know that only one leaf(left or right) is None does not count depth0"""
        if not root:
            return 0
        l = 1+self.minDepth(root.left)
        r = 1+self.minDepth(root.right)
        if l == 1 or r == 1:
            return max(l,r)
        return min(l,r)