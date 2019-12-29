from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = defaultdict(int)
        N = len(nums)
        
        for i in nums:
            counts[i] += 1
            if counts[i] > (N/2):
                return i
