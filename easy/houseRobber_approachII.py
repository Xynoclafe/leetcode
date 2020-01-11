class Solution:
    def rob(self, nums: List[int]) -> int:
        
        secondMax = 0
        firstMax = 0
        for i in nums:
            temp = firstMax
            firstMax = max(secondMax + i, firstMax)
            secondMax = temp
        
        return firstMax