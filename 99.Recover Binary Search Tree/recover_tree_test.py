import unittest
import recover_tree_iteraction as ri


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class RecoverTreeTest(unittest.TestCase):
    def test_find_first_error_node(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(2)
        ri.Solution().recoverTree(root)
        print root