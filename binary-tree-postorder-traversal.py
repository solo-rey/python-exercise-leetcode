class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        nodes = []
        if not root:
            return nodes
        self.helper(root,nodes)
        return nodes

    def helper(self,root,nodes):
        if not root:
            return
        self.helper(root.left,nodes)
        self.helper(root.right,nodes)
        nodes.append(root.val)