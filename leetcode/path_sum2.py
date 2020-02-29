# 113. 路径总和 II  https://leetcode-cn.com/problems/path-sum-ii/submissions/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def do_get_path_sum(node, last):
            if node is not None:
                self.list.append(node.val)
                if last == node.val and node.left is None and node.right is None:
                    self.rs.append(self.list[:])
                else:
                    do_get_path_sum(node.left, last - node.val)
                    do_get_path_sum(node.right, last - node.val)
                self.list.pop()
        self.list = []
        self.rs = []
        do_get_path_sum(root, sum)
        return self.rs
