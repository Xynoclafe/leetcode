class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        totSum = sum(nums)
        minSum = sum(set(nums))
        
        return 2 * minSum - totSum
