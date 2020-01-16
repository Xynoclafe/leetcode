from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        counts = defaultdict(int)
        
        
        def findLengths(word, remWords):
            if counts[word]:
                return counts[word]
            setWords = set(remWords)
            count = 0
            newWords = set({})
            for i in range(len(word)):
                if i < len(word) - 1:
                    newWords.add(word[:i] + word[i + 1:])
                else:
                    newWords.add(word[:i])
            for word2 in newWords:
                nextCount = 0
                if word2 in setWords:
                    nextCount += 1
                    index = remWords.index(word2)
                    if index < len(remWords) - 1:
                        nextCount += findLengths(word2, remWords[index + 1:])
                count = max(count, nextCount)
            counts[word] = count
            return count
                
        words = sorted(words, key = lambda x:len(x), reverse = True)
        maxCount = 0
        for i in range(len(words)):
            word = words[i]
            if i < len(words) - 1:
                curCount = findLengths(word, words[i + 1:]) + 1
            maxCount = max(maxCount, curCount)
        
        return maxCount
        