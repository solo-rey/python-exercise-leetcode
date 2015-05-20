class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    """every layer needs to multiply by 10"""
    def sumHelper(self,root,tmpresult,total):
        if not root:
            return total
        if not root.left and not root.right:
            tmpresult*=10
            tmpresult+=root.val
            total+=tmpresult
            return total
        return self.sumHelper(root.left,tmpresult*10+root.val,total)+self.sumHelper(root.right,tmpresult*10+root.val,total)



    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumHelper(root,0,0)