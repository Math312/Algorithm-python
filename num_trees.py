# 96  https://leetcode-cn.com/problems/unique-binary-search-trees/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        list = [1,1,2]
        if n == 0 or n == 1:
            return 1
        for i in range(2,n):
            temp = 0
            j = 0
            while j <= i:
                temp += list[j]*list[i - j]
                j += 1
            list.append(temp)
        return list[n]

if __name__ == '__main__':
    s = Solution()
    print s.numTrees(3)