class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        largest = [0] * len(nums)
        for i in range(len(nums)):
            maxVal = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxVal = max(maxVal, largest[j])
            largest[i] = maxVal + 1
        return max(largest)
        
