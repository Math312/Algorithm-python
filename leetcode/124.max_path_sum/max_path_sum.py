# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rs = float('-inf')
        def max_gain(node):
            if not node:
                return 0
            max_left = max(max_gain(node.left),0)
            max_right = max(0,max_gain(node.right))
            self.rs = max(self.rs, node.val + max_left + max_right)
            sum = node.val + max(max_left,max_right)
            return sum
        max_gain(root)
        return self.rs