class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def next(data, start):
            def isMax(nums_data, start):
                pre = float('inf')
                for i in range(start,len(nums_data)):
                    if nums_data[i] > pre:
                        return False
                    pre = nums_data[i]
                return True

            def find_next_larger_num(lists, value,start):
                rs = float("inf")
                index = None
                for i in range(start,len(lists)):
                    if rs > lists[i] > value:
                        rs = lists[i]
                        index = i
                return index

            def sort(sort_list, sort_star, end):
                for i in range(sort_star, end):
                    for j in range(i + 1,end):
                        if sort_list[i] > sort_list[j]:
                            sort_temp = sort_list[i]
                            sort_list[i] = sort_list[j]
                            sort_list[j] = sort_temp

            if len(data)-start == 1:
                return data
            else:
                if isMax(data,start):
                    list.sort(data)
                else:
                    if isMax(nums, start + 1):
                        temp_index = find_next_larger_num(data,data[start],start)
                        temp = data[temp_index]
                        data[temp_index] = data[start]
                        data[start] = temp
                        sort(data,start+1,len(nums))
                    else:
                        next(data,start + 1)
        next(nums, 0)
if __name__ == '__main__':
    A = [2,1,3]
    Solution().nextPermutation(A)
    print A




