from collections import defaultdict
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        flag1 = False
        flag2 = False
        
        minDist = 10 ** 10
        
        i1 = -1
        i2 = -1
        
        for i in range(len(words)):
            
            word = words[i]
            
            if word == word1:
                i1 = i
                flag1 = True
            
            elif word == word2:
                i2 = i
                flag2 = True
                
            if flag1 and flag2:
                minDist = min(minDist, abs(i1 - i2))
        
        return minDist