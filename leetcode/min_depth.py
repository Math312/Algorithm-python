# coding=utf-8
# 111. 二叉树的最小深度
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def do_get_min_depth(node):
            list = [node]
            deepth = 1
            next_level_first = node.left
            while len(list) > 0:
                temp = list[0]
                if temp == next_level_first:
                    if len(list) < pow(2, deepth):
                        return deepth
                    else:
                        deepth += 1
                        next_level_first = temp.left
                if temp.left:
                    list.append(temp.left)
                if temp.right:
                    list.append(temp.right)
                list.remove(temp)
            return deepth
        if not root:
            return 0
        if root.left and root.right:
            return do_get_min_depth(root)
        if not root.left:
            return 1+do_get_min_depth(root.right)
        if not root.right :
            return 1 + do_get_min_depth(root.left)

    def minDepth(self, root):
        def min_depth(root):                                    # 获得以root为根结点的树的最小深度
            if not root:
                return 0
            left_min_depth = min_depth(root.left)               # 递归获得左子树的最小深度
            right_min_depth = min_depth(root.right)             # 递归获得右子树的最小深度
            if left_min_depth > 0 and right_min_depth > 0:      # 如果左右子树最小深度都不是0
                res = min(left_min_depth, right_min_depth) + 1  # 当前子树的最小深度是两者较小值+1
            else:                                               # 如果有一个子树是空
                res = max(left_min_depth, right_min_depth) + 1      # 当前数的最小深度取决于非空子树，其深度+1
            return res

        return min_depth(root)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    r1 = TreeNode(20)
    r1.left = TreeNode(15)
    r1.right = TreeNode(7)
    root.right = r1
    s = Solution()
    print s.minDepth(root)