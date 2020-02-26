# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        index = 0
        rs = None
        def in_order_traverse(node):
            if node.left:
                in_order_traverse(node.left)
            if index == k:
                rs = node.val
            if node.right:
                in_order_traverse(node.right)
        in_order_traverse(root)
        return rs