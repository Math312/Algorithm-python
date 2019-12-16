# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def buildTree(pre_order,in_order,pre_start,pre_len,in_start,in_len):
            if in_len == 0 and pre_len == 0:
                return None
            val = pre_order[pre_start]
            in_index = in_order_get_index(in_order,in_start,in_len,val)
            len = in_index-in_start
            node = TreeNode(val)
            node.left = buildTree(pre_order,in_order,pre_start+1,len,in_start,len)
            node.right = buildTree(pre_order, in_order, pre_start + 1 + len, pre_len-len-1, in_index+1, in_len-len-1)
            return node

        def in_order_get_index(in_order,in_start,in_len,split_num):
            i = 0
            while i < in_len:
                if in_order[i+in_start] == split_num:
                    return i+in_start
                i += 1
        return buildTree(preorder,inorder,0,len(preorder),0,len(inorder))


if __name__ == '__main__':
    s = Solution()
    node =  s.buildTree([3, 9, 20, 15, 7],[9, 3, 15, 20, 7])
    print node.val
