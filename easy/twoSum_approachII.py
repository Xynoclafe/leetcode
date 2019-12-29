from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        vals = defaultdict(lambda: -(10 ** 10))
        for i in range(len(nums)):
            if vals[target - nums[i]] == -(10 ** 10):
                vals[nums[i]] = i
            else:
                return [i, vals[target-nums[i]]]
