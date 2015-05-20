class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def mirror(node):
    if node is None:
        return
    mirror(node.left)
    mirror(node.right)
    temp = node.left
    node.left = node.right
    node.right = node.left
