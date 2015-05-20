class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder_incorrect(self, root):
        if not root:
            return []
        current,res = [],[]
        flag =  True
        current.append(root)
        while current:
            next,val = [],[]
            for node in current:
                val.append(node.val)
                if flag:
                    if node.right:
                        next.append(node.right)
                    if node.left:
                        next.append(node.left)
                else:
                    temp = []
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            res.append(val)
            current = next
            if flag:
                flag = False
            else:
                flag = True
        return res

    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def zigzagLevelOrder(self, root):
        res=[]
        self.preorder(root, 0, res)
        return res


s= Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t3.right = t5
print s.zigzagLevelOrder(t1)

