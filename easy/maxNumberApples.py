class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        
        runningSum = 0
        count = 0
        
        for apple in arr:
            runningSum += apple
            if runningSum > 5000:
                break
            else:
                count += 1
        
        return count
