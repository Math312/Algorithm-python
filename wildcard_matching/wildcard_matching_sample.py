# coding=utf-8
# 44. 通配符匹配
# https://leetcode-cn.com/problems/wildcard-matching/
# 贪心算法

"""
该方法是最简单的递归解法

我们知道只有当两字符串同时遍历完则正匹配成功
如果出现模式串匹配完毕，但是字符串串没有匹配完毕的情况，则匹配失败
如果出现字符串匹配完毕，但是模式串没有匹配完毕的情况，则再要考虑

如果模式串最后一个字符是×
那么字符串剩下任何数据都将匹配成功，否则匹配失败

该方法的特点是实现简单，缺点是效率太低，传统递归本身效率就很低，由于它做了很多重复运算。

因此我们考虑优化该方法，减少重复运算
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        return self.character_match(s, 0, p, 0)

    def character_match(self, s, s_index, pattern, pattern_index):
        # 两个字符串同时匹配完成，返回True
        if s_index == len(s) and pattern_index == len(pattern):
            return True
        if pattern_index < len(pattern):
            # 处理×
            if pattern[pattern_index] == '*':
                if s_index == len(s):
                    return self.character_match(s, s_index, pattern, pattern_index + 1)
                # 匹配0个字符  即×代表0个字符的情况
                # 匹配1个字符  即×代表1个字符的情况
                # 匹配多个字符 即×代表多个字符的情况
                return \
                    self.character_match(s, s_index + 1, pattern, pattern_index) or \
                    self.character_match(s, s_index + 1, pattern, pattern_index + 1) or \
                    self.character_match(s, s_index, pattern, pattern_index + 1)
            if s_index < len(s):
                # 处理?
                if pattern[pattern_index] == '?':
                    return self.character_match(s, s_index + 1, pattern, pattern_index + 1)
                # 处理a-z
                else:
                    return pattern[pattern_index] == s[s_index] and self.character_match(s, s_index + 1, pattern,
                                                                                         pattern_index + 1)
            else:
                return False
        # 两个字符串有一个没有匹配完成，都返回False
        if s_index < len(s) and pattern_index == len(pattern):
            return False
