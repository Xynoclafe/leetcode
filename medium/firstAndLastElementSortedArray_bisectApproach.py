import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        x = bisect.bisect(nums, target - 0.1)
        y = bisect.bisect(nums, target + 0.1)
        
        if x == y:
            return [-1, -1]
        
        else:
            return [x, y - 1]
