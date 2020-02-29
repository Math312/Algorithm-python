# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def find_last_node(n, length):
            i = 0
            while i < length-1:
                if n:
                    n = n.next
                else:
                    return None
                i += 1
            return n
        if k == 1:
            return head
        pre = None
        p0 = head
        p1 = head
        p1 = find_last_node(p1, k)
        if not p1:
            return head
        head = p1
        while True:
            temp = None
            if p1:
                temp = p1.next
                temp2 = p0
                temp3 = temp2.next
                while temp2 and temp2 != p1:
                    temp4 = temp3.next
                    temp3.next = temp2
                    temp2 = temp3
                    temp3 = temp4
            if pre:
                if p1:
                    pre.next = p1
                else:
                    pre.next = p0
                    break
            pre = p0
            if temp:
                p0 = temp
                p1 = find_last_node(p0, k)
            else:
                pre.next=None
                break
        return head
