class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    maxv = -99999
    def maxhelp(self,root):
        if not root:
            return 0
        l = max(0,self.maxhelp(root.left))
        r = max(0,self.maxhelp(root.right))
        tot = root.val
        if l > 0:
            tot+=l
        if r > 0:
            tot+=r
        self.maxv = max(self.maxv,tot)
        return root.val+max(l,r)

    def maxPathSum(self, root):
        if not root:
            return 0
        self.maxhelp(root)
        return self.maxv

