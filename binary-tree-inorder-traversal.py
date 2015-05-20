class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    nodes = []
    def inorderTraversal(self, root):
        self.helper(root)
        return self.nodes

    def helper(self,root):
        if not root:
            return
        self.nodes.extend(self.inorderTraversal(root.left))
        self.nodes.append(root.val)
        self.nodes.extend(self.inorderTraversal(root.right))
        return self.nodes


"""local variable is faster than instance variable"""
def inorderTraversal(self, root):
    nodes = []
    self.helper(root,nodes)
    return nodes

def helper(self,root,nodes):
    if not root:
        return
    self.helper(root.left,nodes)
    nodes.append(root.val)
    self.helper(root.right,nodes)
    return nodes
