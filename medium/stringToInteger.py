from collections import deque
class Solution:
    def myAtoi(self, str: str) -> int:
        negative = False
        queue = deque()
        sign = True
        
        nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        
        for char in str:
            if char == "-" and sign:
                sign = False
                negative = True
            elif char == "+" and sign:
                sign = False
            elif char == " ":
                if not sign:
                    break
            elif char in nums:
                if sign:
                    sign = False
                queue.append(char)
            else:
                break
        
        runningSum = 0
        while queue:
            num = queue.popleft()
            if num in nums:
                runningSum = runningSum * 10 + nums[num]
            if runningSum >= pow(2, 31):
                return - pow(2,31) if negative else pow(2,31) - 1
        
        return -runningSum if negative else runningSum
