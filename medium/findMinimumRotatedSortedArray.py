class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        
        if nums[end] > nums[0]:
            return nums[0]
        
        while(start < end):
            pivot = (start + end) // 2
            
            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            
            if nums[pivot] < nums[pivot - 1]:
                return nums[pivot]
            
            if nums[pivot] > nums[0]:
                start = pivot + 1
            
            else:
                end = pivot - 1
        
        return nums[start]
