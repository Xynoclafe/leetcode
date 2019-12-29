class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        visited = set({})
        l1 = []
        l2 = []
        l1.append(0)
        while len(l1) > 0:
            i = l1.pop(0)
            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet and j + 1 not in visited:
                    l2.append(j + 1)
                    visited.add(j + 1)
            if len(l1) == 0:
                l1 = l2
                l2 = []
        length = len(s)
        if length in visited:
            return True
        else:
            return False
