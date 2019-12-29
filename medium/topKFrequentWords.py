from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCounts = defaultdict(int)
        for word in words:
            wordCounts[word] += 1
        countList = []
        wordList = set(words)
        for word in wordList:
            countList.append([wordCounts[word], word])
        countList.sort(reverse=True)
        returnList = []
        prevCount = countList[0][0]
        i = 0
        commonList = []
        while True:
            if countList[i][0] < prevCount:
                commonList.sort()
                for word in commonList:
                    returnList.append(word)
                commonList = []
                prevCount = countList[i][0]
                commonList.append(countList[i][1])
            else:
                prevCount = countList[i][0]
                commonList.append(countList[i][1])
            i += 1
            if(i >= k):
                if(i >= len(countList) or countList[i][0] < prevCount):
                    commonList.sort()
                    for word in commonList:
                        returnList.append(word)
                    break
                else:
                    continue
        return returnList[:k]
