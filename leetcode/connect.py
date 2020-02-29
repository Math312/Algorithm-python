# coding=utf-8
# 116. 填充每个节点的下一个右侧节点指针
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def do_connect(node):
            if node:
                if node.left:
                    node.left.next = node.right
                if node.right and node.next:
                    node.right.next = node.next.left
                do_connect(node.left)
                do_connect(node.right)
                return node
        return do_connect(root)

    def connect2(self, root):
        cur = root
        next_level_first = root.left
        while cur:
            if cur == next_level_first:
                next_level_first = cur.left
            if cur.left:
                cur.left.next = cur.right
            if cur.next and cur.right:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = next_level_first
        return root

    def connect3(self, root):
        # if root is None
        if root is None:
            return

        the_root = root

        while root.left is not None:
            next_layer = root.left
            while root.next is not None:
                root.left.next = root.right
                root.right.next = root.next.left
                root = root.next
            root.left.next = root.right
            root = next_layer
        return the_root

if __name__ == '__main__':
    l1 = Node(2,Node(4),Node(5))
    r1 = Node(3,Node(6),Node(7))
    root = Node(1,l1,r1)
    s = Solution()
    rs = s.connect2(root)
    print rs.val