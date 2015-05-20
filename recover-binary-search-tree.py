class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node

    def recoverTree(self, root):
        if not root:
            return
        self.n1,self.n2 = None,None
        self.pre = None
        self.helper(root)
        self.n1.val,self.n2.val = self.n2.val,self.n1.val
        return root


    def helper(self,root):
        if not root:
            return
        self.helper(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.n1:
                self.n1,self.n2 = self.pre,root
            else:
                self.n2 = root
        self.pre = root
        self.helper(root.right)
