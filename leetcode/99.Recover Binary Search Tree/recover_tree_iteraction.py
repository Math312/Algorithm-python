# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def find_first_error_node(node):
            stack = [node]
            pre = float("-inf")
            rs = None
            while len(stack) > 0:
                source_node = stack.pop()
                temp = source_node
                stack.append(temp)
                while temp.left:
                    stack.append(temp.left)
                    temp = temp.left
                temp3 = source_node
                while temp3 == source_node and len(stack) > 0:
                    temp = stack.pop()
                    if temp.val >= pre:
                        pre = temp.val
                    else:
                        rs = temp
                        pre = temp.val
                    if temp.right:
                        stack.append(temp.right)
                        temp3 = temp.right
            return rs

        def find_other_error_node(node, first_error_node):
            stack = [node]
            while len(stack) > 0:
                source_node = stack.pop()
                temp = source_node
                stack.append(temp)
                while temp.left:
                    stack.append(temp.left)
                    temp = temp.left
                temp3 = source_node
                while temp3 == source_node and len(stack) > 0:
                    temp = stack.pop()
                    if temp.val > first_error_node.val:
                        return temp
                    if temp.right:
                        stack.append(temp.right)
                        temp3 = temp.right

        first_error_node1 = find_first_error_node(root)
        other_error_node = find_other_error_node(root,first_error_node1)
        temp = first_error_node1.val
        first_error_node1.val = other_error_node.val
        other_error_node.val = temp
