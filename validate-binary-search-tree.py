class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        nodes = []
        return self.helper(root,nodes)

    def helper(self,root,nodes):
        if not root:
            return True
        left = self.helper(root.left,nodes)
        if not nodes:
            nodes.append(root.val)
        else:
            if nodes[-1] >= root.val:
                return False
            nodes.append(root.val)
        right = self.helper(root.right,nodes)
        return left and right
