# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def doInorderTraversal(self,root, result):
        if root is not None:
            if root.left is not None:
                self.doInorderTraversal(root.left, result)
            result.append(root.val)
            if root.right is not None:
                self.doInorderTraversal(root.right, result)

    def inorderTraversal(self, root):
        result = []
        self.doInorderTraversal(root, result)
        return result
    #
    # def doInorderTraversal(self,root):
    #     min