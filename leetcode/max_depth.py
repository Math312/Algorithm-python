# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def in_order_traversal(node,level):
            if node:
                in_order_traversal(node.left,level+1)
                self.max_depth = max(self.max_depth,level+1)
                in_order_traversal(node.right, level + 1)
        self.max_depth = 0
        in_order_traversal(root,0)
        return self.max_depth