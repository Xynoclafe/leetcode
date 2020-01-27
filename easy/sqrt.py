class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        low = 2
        up = x // 2
        
        while(low <= up):
            pivot = (low + up) // 2
            
            sq = pivot * pivot
            if sq > x:
                up = pivot - 1
            elif sq < x:
                low = pivot + 1
            else:
                return pivot
        
        return up
