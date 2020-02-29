# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inorder(node):
            if node:
                rs = True
                if node.left:
                    rs = rs and inorder(node.left)
                if self.pre is None:
                    self.pre = node.val
                else:
                    rs = rs and (node.val > self.pre)
                    self.pre = node.val
                if node.right:
                    rs = rs and inorder(node.right)
                return rs
            return True
        self.pre = None
        return inorder(root)
