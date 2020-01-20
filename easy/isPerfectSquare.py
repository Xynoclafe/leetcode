class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return True
        
        minm = 2
        maxm = num // 2
        
        while(minm <= maxm):
            pivot = (minm + maxm) // 2
            
            square = pivot * pivot
            
            if square == num:
                return True
            
            elif square < num:
                minm = pivot + 1
            
            else:
                maxm = pivot - 1
        
        return False
