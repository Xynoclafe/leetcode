from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        repeats = defaultdict(lambda: -1)
        
        for i in range(len(nums)):
            num = nums[i]
            if repeats[num] != -1:
                return True
            else:
                repeats[num] = i
        
        return False
