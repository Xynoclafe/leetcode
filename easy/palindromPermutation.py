from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        seen = defaultdict(int)
        for char in s:
            seen[char] += 1
        
        flag = True
        for key in seen:
            if seen[key] % 2 != 0:
                if flag:
                    flag = False
                else:
                    return False
        return True