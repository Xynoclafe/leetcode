from collections import deque
class Solution:
    def removeVowels(self, S: str) -> str:
        newString = deque([])
        for s in S:
            if s not in {"a", "e", "i", "o", "u"}:
                newString.append(s)
        
        return "".join(s for s in newString)
        