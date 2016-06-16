"""
Invert a binary tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree_recusive(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        tmp = root.left
        root.left = self.invertTree_recusive(root.right)
        root.right = self.invertTree_recusive(tmp)
        return root

    def invertTree_iterator(self, root):
        if root == None:
            return root
        q = []
        q.append(root)
        while len(q) > 0:
            node = q[-1]
            q.pop()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root

