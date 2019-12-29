from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1
        uniqueNums = set(nums)
        countNums = []
        for num in uniqueNums:
            countNums.append([numCount[num], num])
        countNums.sort(reverse = True)
        return [countNums[i][1] for i in range(k)]
