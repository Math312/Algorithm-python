class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        dp = [0]*len(s)
        count = 0
        for index in range(1,len(s)):
            if s[index] == ')' and s[index - 1] == '(':
                dp[index] = dp[index-2] + 2
                continue
            if s[index] == ')' and s[index-1] == ')' and s[index - dp[index-1] -1] == '(':
                  dp[index] = dp[index-1]+ 2 + dp[index - dp[index-1] -2]
        rs = dp[0]
        rs = dp[0]
        for i in dp:
            if rs < i:
                rs = i
        return rs
