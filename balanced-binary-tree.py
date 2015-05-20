class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        return self.helper(root) >= 1

    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left < 0 or right < 0:
            return -1
        if (left-right)>=2 or (left-right)<=-2:
            return -1
        return max(left,right)+1