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
        stack = []
        num = 0
        while head:
            num += 1
            stack.append(head)
            head = head.next
        if num > 0:
            head = stack.pop()
            temp = head
            num -= 1
            while num > 0:
                num -= 1
                temp.next = stack.pop()
                temp = temp.next
            temp.next = None
        return head
