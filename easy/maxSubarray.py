class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = -(10**10)
        for num in nums:
            sum = max(num, sum + num)
            maxSum = max(maxSum, sum)
        return maxSum
                    
