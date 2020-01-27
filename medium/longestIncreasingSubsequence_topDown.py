class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        maxScores = [[-1 for _ in range(len(nums) + 1)]for _ in range(len(nums))]
        
        def maxLength(curPos, prevPos):
            if curPos == len(nums):
                return 0
            
            if maxScores[curPos][prevPos + 1] != -1:
                return maxScores[curPos][prevPos + 1]
            
            included = 0
            if prevPos < 0 or nums[curPos] > nums[prevPos]:
                included = 1 + maxLength(curPos + 1, curPos)
            
            excluded = maxLength(curPos + 1, prevPos)
            
            maxScores[curPos][prevPos + 1] = max(included, excluded)
            
            return maxScores[curPos][prevPos + 1]
        
        return maxLength(0, -1)
