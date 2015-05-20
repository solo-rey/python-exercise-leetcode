# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)



class Solution:
    # @return a list of tree node

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


    def generateTrees(self, n):
        res = self.generateTrees1(1,n)
        """
        for node in res:
            nodea = self.postorderTraversal(node)
            print nodea
        """
        return res

    def generateTrees1(self,left,right):
        res = []
        if left > right:
            res.append(None)
            return res
        for i in range(left,right+1):
            lefts = self.generateTrees1(left,i-1)
            rights = self.generateTrees1(i+1,right)
            for j in range(len(lefts)):
                for k in range(len(rights)):
                    root = TreeNode(i)
                    root.left = lefts[j]
                    root.right = rights[k]
                    """
                    if root.left:
                        print "left: "+str(root)+" "+str(root.left)
                    if root.right:
                        print "right: "+str(root)+" "+str(root.right)
                    nodea = self.postorderTraversal(root)
                    print nodea
                    """
                    res.append(root)
        return res


s = Solution()
s.generateTrees(4)


