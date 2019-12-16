# coding=utf-8
# 110. 平衡二叉树
# https://leetcode-cn.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def deepth(root):
            if not root:
                return 0
            else:
                left_deepth = deepth(root.left)
                right_deepth = deepth(root.right)
                if abs(right_deepth - left_deepth) > 1:
                    self.rs = False;
                return max(left_deepth,right_deepth)+1
        self.rs = True
        deepth(root)
        return self.rs
