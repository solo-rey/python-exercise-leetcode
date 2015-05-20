class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Solution:

    def insertBST(self,root,x):
        if root is None:
            node = TreeNode(x)
            return node
        self.helper(root,x)


    def helper(self,root,x):
        if root is None:
            return
        if root.val == x:
            return
        elif root.val > x:
            if root.left:
                self.helper(root.left,x)
            else:
                node = TreeNode(x)
                root.left = node
        elif root.val < x:
            if root.right:
                self.helper(root.right,x)
            else:
                node = TreeNode(x)
                root.right = node