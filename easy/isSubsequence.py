class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
        ptr = 0
        length = len(s)
        for char in t:
            if char == s[ptr]:
                ptr += 1
                if ptr == length:
                    return True
        
        return False