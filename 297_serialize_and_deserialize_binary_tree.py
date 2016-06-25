"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        st = ''

        def _serialize(root, st):
            tmp_st = ''
            if root:
                tmp_st = (str(root.val) + ' ')
                tmp_st += _serialize(root.left, st)
                tmp_st += _serialize(root.right, st)

            else:
                tmp_st = '# '
            st += tmp_st
            return st
        return _serialize(root, st)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split()
        def _deserialize(data_list):

            tmp_node = data_list.pop(0)
            if tmp_node == '#':
                return None
            root = TreeNode(int(tmp_node))
            root.left = _deserialize(data_list)
            root.right = _deserialize(data_list)
            return root
        return _deserialize(data_list)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def preorder(root):
    if root is None:
        print ' '
        return
    print str(root.val) + ' '
    preorder(root.left)
    preorder(root.right)
    return

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
codec = Codec()
"""
1 2 # # 3 4 # # 5 # #
"""
# print codec.serialize(node1)
root = codec.deserialize(codec.serialize(node1))
preorder(root)
