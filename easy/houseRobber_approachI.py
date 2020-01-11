class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        
        maxm = [0] * len(nums)
        
        maxm[0] = nums[0]
        maxm[1] = nums[1]
        
        n = len(nums)
        
        for i in range(2, n):
            maxm[i] = max(maxm[0:i-1]) + nums[i]
        
        return max(maxm[n-1], maxm[n-2])