class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def path(root,sum,target):
    if not root:
        return False
    if not root.left:
        return path(root.right,sum,target)
    if not root.right:
        return path(root.left,sum,target)
    if sum+root.val == target:
        return True
    else:
        return path(root.left,sum+root.val,target) or path(root.right,sum+root.val,target)



# @param root, a tree node
# @param sum, an integer
# @return a boolean
def hasPathSum(root, sum):
    return path(root,0,sum)

