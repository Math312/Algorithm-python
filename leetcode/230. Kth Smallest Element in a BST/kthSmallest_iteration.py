# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        node = root
        stack = []
        index = 0
        while node:
            stack.append(node)
            temp = node.left
            while temp:
                stack.append(temp)
                temp = temp.left
            temp2 = node
            while node == temp2:
                temp = stack.pop()
                index += 1
                if index == k:
                    return temp.val
                else:
                    if temp.right:
                        node = temp.right
