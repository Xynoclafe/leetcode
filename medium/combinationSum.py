class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def soln(candidates, nums, runningSum, target):
            runningSum += candidates[0]
            nums.append(candidates[0])
            if runningSum > target:
                return
            if runningSum == target:
                returnList.append(nums)
            if runningSum < target:
                for i in range(len(candidates)):
                    soln(candidates[i:], nums.copy(), runningSum, target)
                return
            
            
        runningSum = 0
        
        candidates.sort()
        
        returnList = []
        
        nums = []
        for i in range(len(candidates)):
            soln(candidates[i:], nums.copy(), runningSum, target)
        
        return returnList
        