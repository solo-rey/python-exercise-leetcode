"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        lst = []
        def _binary(root, st):
            if not root:
                return
            if st == "":
                st = str(root.val)
            else:
                st += ("->" + str(root.val))
            if root.left:
                _binary(root.left, st)
            if root.right:
                _binary(root.right, st)
            if not root.left and not root.right:
                lst.append(st)
            # if root.right:
            #     _binary(root.right, st)
        _binary(root, "")
        return lst


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)
node1.left = node2
node2.right = node5
node1.right = node3

s = Solution()
print s.binaryTreePaths(node1)
