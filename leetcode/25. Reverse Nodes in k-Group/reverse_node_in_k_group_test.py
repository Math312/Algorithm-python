import unittest
import reverse_nodes_in_k_group as rsikg


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ReverseNodeInKGroupTest(unittest.TestCase):

    def test_reverse_k_group(self):
        s = rsikg.Solution()
        root = ListNode(1)
        root.next = ListNode(2)
        s.reverseKGroup(root, 2)