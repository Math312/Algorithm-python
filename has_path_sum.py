# 112. 路径总和 https://leetcode-cn.com/problems/path-sum/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def do_has_path_sum(node,sum):
            if node is not None:
                self.list.append(node.val)
                temp = sum - node.val
                if temp == 0 and node.left is None and node.right is None:
                    self.result = True
                do_has_path_sum(node.left,temp)
                do_has_path_sum(node.right,temp)
                self.list.pop()
        self.list = []
        self.result = False
        do_has_path_sum(root,sum)
        return self.result

if __name__ == '__main__':
    s = Solution()
    r = TreeNode(-2)
    r.right = TreeNode(-3)
    print s.hasPathSum(r,-5)