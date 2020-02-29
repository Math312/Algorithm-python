# 102. 二叉树的层次遍历 https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        list = [root]
        first = None
        rs_in = []
        rs = []
        while list.__len__() > 0:
            temp = list[0]
            if temp == first:
                rs.append(rs_in[:])
                rs_in = []
                first = None
            rs_in.append(temp.val)
            if temp.left:
                list.append(temp.left)
                if not first:
                    first = temp.left
            if temp.right:
                list.append(temp.right)
                if not first:
                    first = temp.right
            list.remove(temp)
        rs.append(rs_in[:])
        return rs

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    r1 = TreeNode(20)
    root.right = r1
    r1.left = TreeNode(15)
    r1.right = TreeNode(7)
    s = Solution()
    print s.zigzagLevelOrder(root)



