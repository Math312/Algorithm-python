import wildcard_matching_sample as wm
import wildcard_matching_optimization_1 as wm1
import wildcard_matching_optimization_2 as wm2
import unittest


class WildcardMatchingTest(unittest.TestCase):
    def test_blank_str(self):
        o = wm2.Solution()
        self.assertTrue(o.isMatch('', '*'))
        self.assertTrue(o.isMatch('', ''))
        self.assertFalse(o.isMatch('', '?'))
        self.assertFalse(o.isMatch('', 'a'))
        self.assertFalse(o.isMatch('a', ''))

    def test_question_mark(self):
        o = wm2.Solution()
        self.assertTrue(o.isMatch('A', '?'))
        self.assertTrue(o.isMatch('Aa', 'A?'))
        self.assertTrue(o.isMatch('aA', 'a?'))
        self.assertFalse(o.isMatch('', '?'))

    def test_star_mark(self):
        o = wm2.Solution()
        self.assertTrue(o.isMatch('A', '*'))
        self.assertTrue(o.isMatch('Aa', '*'))
        self.assertTrue(o.isMatch('', '*'))

    def test_comprehensive(self):
        o = wm2.Solution()
        self.assertTrue(o.isMatch("A", "A*"))
        self.assertTrue(o.isMatch('abcbdk','*a*b?k'))
        self.assertTrue(o.isMatch("aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab","*ab***ba**b*b*aaab*b"))
        self.assertFalse(o.isMatch("zacabz","*a?b*"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WildcardMatchingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
