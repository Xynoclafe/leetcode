class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minList = [i+1 for i in range(len(nums) + 1)]
        print(minList)
        for item in nums:
            if item <= len(nums) and item > 0:
                minList[item - 1] = 0
        print(minList)
        for item in minList:
            if item > 0:
                return item
