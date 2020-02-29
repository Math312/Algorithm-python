class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = len(nums)-1
        p = 0
        while p <= p1:
            if nums[p] == val:
                temp = nums[p1]
                nums[p1] = nums[p]
                nums[p] = temp
                p1 -= 1
            else:
                p += 1
        return p