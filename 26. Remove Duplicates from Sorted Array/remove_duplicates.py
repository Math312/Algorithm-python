class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        index = 1
        record = nums[0]
        for i in range(1,len(nums)):
            if record != nums[i]:
                nums[index] = nums[i]
                index += 1
                record = nums[i]
        return index