class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        if nums[high] > nums[low]:
            return nums[low]
        
        while low < high:
            pivot = low + (high - low) // 2
            
            if nums[pivot] < nums[high]:
                high = pivot
            
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            
            else:
                high -= 1
        
        return nums[high]
