class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_num = 0
        max_num = nums[0]
        for i in nums:
            sum_num += i
            max_num = max(sum_num, max_num)
            if sum_num < 0:
                sum_num = 0
        return max_num
