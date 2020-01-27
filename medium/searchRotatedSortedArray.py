class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(nums, start, end, flag, find = 0):
            if flag:
                pivot = (start + end)//2
                if pivot == len(nums) - 1:
                    return 0
                elif nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                elif nums[pivot] < nums[start]:
                    return binarySearch(nums, start, pivot - 1, flag)
                else:
                    return binarySearch(nums, pivot + 1, end, flag)
            else:
                pivot = (start + end)//2
                if nums[pivot] == find:
                    return pivot
                elif start >= end:
                    return -1
                elif nums[pivot] > find:
                    return binarySearch(nums, start, pivot - 1, flag, find)
                else:
                    return binarySearch(nums, pivot + 1, end, flag, find)
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        low = binarySearch(nums, 0, len(nums) - 1, True)
        if low == 0:
            return binarySearch(nums, 0, len(nums) - 1, False, target)
        if nums[0] > target:
            return binarySearch(nums, low, len(nums) - 1, False, target)
        else:
            return binarySearch(nums, 0, low - 1, False, target)