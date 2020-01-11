from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = defaultdict(int)
        runningSum = 0
        ans = 0
        
        for num in nums:
            runningSum += num
            
            if runningSum == k:
                ans += 1
                
            if sums[runningSum - k] != 0:
                ans += sums[runningSum - k]
                
            sums[runningSum] += 1
        
        return ans