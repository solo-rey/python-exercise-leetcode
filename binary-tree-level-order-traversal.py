class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        current,res = [root], []
        while current:
            nextnode,val = [],[]
            for node in current:
                val.append(node.val)
                if node.left:
                    nextnode.append(node.left)
                if node.right:
                    nextnode.append(node.right)
            res.append(val)
            current = nextnode
        return res


    def levelOrder1(self,root):
        if not root:
            return []
        current,res = [], []
        current.append(root)
        while current:
            next,var = [],[]
            for node in current:
                val.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            res.append(val)
            current = next
        return res


