from collections import defaultdict
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        possible = defaultdict(lambda: None)
        
        if len(nums) == 1:
            return True
        
        def jumps(start, end):
            if possible[start] is not None:
                return possible[start]
            if start >= end:
                return True
            else:
                A = []
                for i in range(1, nums[start] + 1):
                    A.append(jumps(start + i, end))
                possible[start] = True if True in A else False
                return possible[start]
        
        return jumps(0, len(nums) - 1)
