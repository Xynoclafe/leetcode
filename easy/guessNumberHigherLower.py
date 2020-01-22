# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def binSearch(start, end):
            if start == end:
                start
            
            pivot = (start + end) // 2
            
            return pivot
        
        start = 0
        end = n
        while True:
            num = binSearch(start, end)
            result = guess(num)
            if result == 0:
                return num
            elif result == 1:
                start = num + 1
            else:
                end = num - 1
