# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def equals(n1,n2):
            if n1 is None and n2 is None:
                return True
            if n1 is not None and n2 is not None:
                return equals(n1.left,n2.right) and equals(n1.right,n2.left) and n1.val == n2.val
            return False
        return equals(root,root)