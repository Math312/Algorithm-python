import unittest
import sunday

class TestSunday(unittest.TestCase):

    def test_find_str(self):
        solution = sunday.Solution()
        self.assertEqual(0,solution.findStr("",""))
        self.assertEqual(0, solution.findStr("A", ""))
        self.assertEqual(0, solution.findStr("ABC", "A"))
        self.assertEqual(1, solution.findStr("BAC", "A"))
        self.assertEqual(2, solution.findStr("hello", "ll"))
        self.assertEqual(-1, solution.findStr("aaaaa", "bba"))
        self.assertEqual(4, solution.findStr("mississippi", "issip"))
        self.assertEqual(9, solution.findStr("mississippi", "pi"))