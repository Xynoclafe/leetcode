from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seen = defaultdict(lambda: False)
        count = 0
        
        for i in range(len(nums)):
            
            if seen[nums[i]]:
                count -= nums[i]
            else:
                count += nums[i]
                seen[nums[i]] = True
        
        return count