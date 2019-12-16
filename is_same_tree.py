# 100. 相同的树  https://leetcode-cn.com/problems/same-tree/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def equals(n1,n2):
            if n1 is None and n2 is None:
                return True
            if n1 is not None and n2 is not None:
                return equals(n1.left,n2.left) and equals(n1.right,n2.right) and n1.val == n2.val
            return False
        return equals(p,q)