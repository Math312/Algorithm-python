import unittest
import kthSmallest_recursive as kth

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class KthSmallestTest(unittest.TestCase):
    def test_comprehensive(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        solution = kth.Solution()
        self.assertEqual(1,solution.kthSmallest(root,1))
