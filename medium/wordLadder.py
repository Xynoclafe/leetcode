from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        if beginWord in wordList:
            wordList.remove(beginWord)
            
            
        allTypesDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                allTypesDict[word[0:i] + "*" + word[i+1:]].append(word)
        
        wordLevels = []
        wordLevels.append([beginWord])
        level = 1
        while(len(wordList) > 0):
            prevWords = wordLevels[level -1]
            curList = []
            for word in prevWords:
                nextLevel = []
                for i in range(len(word)):
                    nextLevel = nextLevel + allTypesDict[word[0:i] + "*" + word[i + 1:]]
                nextLevel = list(set(wordList).intersection(set(nextLevel)))
                for tWord in nextLevel:
                    curList.append(tWord)
                    wordList.remove(tWord)
                    if tWord == endWord:
                        return level + 1
            wordLevels.append(curList)
            if len(curList) == 0 and len(wordList) != 0:
                return 0
            level += 1
        return level
        
        
        
