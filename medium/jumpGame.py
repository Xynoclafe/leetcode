class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if n == 1:
            return True
        
        maxIndex = 0
        
        for i in range(n):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i + nums[i])
            if maxIndex >= n - 1:
                return True
        
        return True
        
