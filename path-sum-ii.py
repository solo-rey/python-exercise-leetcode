class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def path(root,sum,target,tmplst,totallist):
    global totallist
    if not root:
        return totallist
    sum+=root.val
    if not root.left and not root.right:
        if sum == target:
            tmplst.append(root)
            totallist.append(tmplst)
            return totallist
        else:
            return totallist
    tmplst.append(root)
    return path(root.left,sum,target,tmplst,totallist).extend(path(root.right,sum,target,tmplst,totallist))


# @param root, a tree node
# @param sum, an integer
# @return a list of lists of integers
def pathSum(root, sum):
    totallist = []
    return path(root,0,sum,[],totallist)



def pathSum(self, root, sum):
    return self.pathSumRecur([], [], root, sum)

def pathSumRecur(self, result, path, root, sum):
    if root is None:
        return result
    if root.left is None and root.right is None and root.val == sum:
        return result + [path + [root.val]]
    return self.pathSumRecur(result, path + [root.val], root.left, sum - root.val) + self.pathSumRecur(result, path + [root.val], root.right, sum - root.val)

