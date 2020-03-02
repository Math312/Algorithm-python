# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p0 = head
        if not p0:
            return head
        p1 = head.next
        p0.next = None
        while p0 and p1:
            temp = p1.next
            p1.next = p0
            p0 = p1
            p1 = temp
        head = p0
