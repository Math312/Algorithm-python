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
            sum_num = max(sum_num, i)
            if sum_num > max_num:
                max_num = sum_num
        return max_num
