class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        else:
            rs = []
            for i in range(0,len(nums)):
                temp = []
                temp.extend(nums)
                temp.pop(i)
                rs_inner = self.permute(temp)
                for j in rs_inner:
                    rs.append([nums[i]]+j)
            return rs