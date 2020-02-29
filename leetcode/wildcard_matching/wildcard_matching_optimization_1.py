# coding=utf-8

"""
首先考察wildcard_matching_sample.py中可能出现重复操作的地方

1.连续多个×其实效果是相同的，但是却会给代码增加很多的递归操作，一个×就是3个递归操作，如果是10个重复的×号，后果不堪设想，因此，优化的第一步是消除重复×号

2.递归最耗费资源的操作是其重复运算的操作过多，因此，我们需要将重复操作记录下来，以后直接查询就可以大大提高效率
"""


def remove_dup_stars(s):
    if s == '':
        return s
    p1 = ''
    label = 0
    for c in s:
        if label != 1 or c != '*':
            p1 += c
            label = 0
        else:
            label = 1
    return p1


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        cache = {}
        processed_str = remove_dup_stars(p)
        self.character_match(s, 0, processed_str, 0,cache)
        if (len(s), len(processed_str)) in cache:
            return cache[(len(s), len(processed_str))]
        return False

    def character_match(self, s, s_index, pattern, pattern_index,cache):
        if (s_index,pattern_index) in cache:
            return cache[(s_index,pattern_index)]
        rs = False
        # 两个字符串同时匹配完成，返回True
        if s_index == len(s) and pattern_index == len(pattern):
            rs = True
        elif pattern_index < len(pattern):
            # 处理×
            if pattern[pattern_index] == '*':
                if s_index == len(s):
                    rs = self.character_match(s, s_index, pattern, pattern_index + 1,cache)
                # 匹配0个字符  即×代表0个字符的情况
                # 匹配1个字符  即×代表1个字符的情况
                # 匹配多个字符 即×代表多个字符的情况
                else:
                    rs = \
                        self.character_match(s, s_index + 1, pattern, pattern_index, cache) or \
                        self.character_match(s, s_index + 1, pattern, pattern_index + 1, cache) or \
                        self.character_match(s, s_index, pattern, pattern_index + 1, cache)
            else:
                if s_index < len(s):
                    # 处理?
                    if pattern[pattern_index] == '?':
                        rs = self.character_match(s, s_index + 1, pattern, pattern_index + 1,cache)
                    # 处理a-z
                    else:
                        rs = pattern[pattern_index] == s[s_index] and self.character_match(s, s_index + 1, pattern,
                                                                                             pattern_index + 1,cache)
                else:
                    rs = False
        # 两个字符串有一个没有匹配完成，都返回False
        else:
            rs = False
        cache[(s_index,pattern_index)] = rs
        return rs
