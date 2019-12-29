class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def findSubWords(word, wordSet, foundWords , i):
            x = i
            found = False
            stopIndex = -1
            for j in range(x, len(word)):
                if s[x:j + 1] in wordSet and (x, j+1) not in foundWords:
                    foundWords.add((x, j + 1))
                    found = True
                    stopIndex = j + 1
                    break
            if not found:
                return False
            if found and stopIndex == len(word):
                return True
            first = findSubWords(word, wordSet, foundWords, i)
            second = findSubWords(word, wordSet, foundWords, stopIndex)
            return first or second
        
        
        return findSubWords(s, set(wordDict), set({}), 0)
