class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}

        def jump(nums, index):
            if nums[index] + index >= len(nums) - 1:
                return True
            else:
                rs = False
                if nums[index] < 1:
                    return rs
                skip = 1
                while skip <= nums[index]:
                    if map.has_key(index + skip):
                        rs = rs or map.get(index + skip)
                    else:
                        temp = jump(nums, index + skip)
                        map[index + skip] = temp
                        rs = rs or temp
                    skip += 1
                return rs

        return jump(nums, 0)


if __name__ == '__main__':
    print Solution().canJump(
        [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0,
         0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0,
         7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6])
