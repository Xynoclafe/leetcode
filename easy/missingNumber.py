class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        arraySum = sum(nums)
        actualSum = (len(nums) * (len(nums) + 1)) // 2
        
        return actualSum - arraySum