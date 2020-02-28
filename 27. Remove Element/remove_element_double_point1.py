class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[p1] = nums[i]
                p1 += 1
        return p1