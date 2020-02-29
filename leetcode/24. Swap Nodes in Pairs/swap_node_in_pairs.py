# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p0=head
        p1=head.next
        if p1:
            head = p1
        pre = None
        while p1:
            p2 = p1.next
            if pre:
                pre.next = p1
            p1.next = p0
            p0.next = p2
            pre = p0
            if p0.next:
                p0 = p0.next
            if p0 and p0.next:
                p1 = p0.next
            else:
                p1 = None
        return head


