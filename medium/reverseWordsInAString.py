from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        strArray = s.split()
        retStr = deque()
        for i in range(1, len(strArray) + 1):
            if(strArray[-i] != ""):
                retStr.append(strArray[-i])
        return " ".join(retStr)
        
