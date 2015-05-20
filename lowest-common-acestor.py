class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Solution:

    def LCA(self, root,p,q):
        if not root or not p or not q:
            return
        if max(p.val,q.val) < root.val:
            return self.LCA(root.left,p,q)
        if min(p.val,q.val) > root.val:
            return self.LCA(root.right,p,q)
        else:
            return root


l1 = TreeNode(6)
l2 = TreeNode(2)
l3 = TreeNode(8)
l4 = TreeNode(0)
l5 = TreeNode(4)
l6 = TreeNode(7)
l7 = TreeNode(9)
l8 = TreeNode(3)
l9 = TreeNode(5)
l1.left = l2
l1.right=l3
l2.left=l4
l2.right=l5
l3.left=l6
l3.right=l7
l5.left=l8
l5.right=l9
s = Solution()
print s.LCA(l1,l6,l3).val
