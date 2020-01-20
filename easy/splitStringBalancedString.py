class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        RCount = 0
        LCount = 0
        
        splits = 0
        
        for char in s:
            if char == "R":
                RCount += 1
            else:
                LCount += 1
            
            if LCount == RCount:
                LCount = 0
                RCount = 0
                splits += 1
        
        return splits
