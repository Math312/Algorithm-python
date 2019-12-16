# coding=utf-8
# 114. 二叉树展开为链表 https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def do_post_order_traversal(node):
            if node:
                do_post_order_traversal(node.right)
                do_post_order_traversal(node.left)

                if not self.pre:
                    self.pre = node
                else:
                    node.right = self.pre
                    self.pre = node
                    node.left = None

        self.pre = None
        do_post_order_traversal(root)
        return root


if __name__ == '__main__':
    root=TreeNode(1)
    l1 = TreeNode(2)
    root.left = l1
    l1.left = TreeNode(3)
    l1.right = TreeNode(4)
    r1 = TreeNode(5)
    root.right = r1
    r1.right = TreeNode(6)
    s = Solution()
    s.flatten(root)
    print root.val