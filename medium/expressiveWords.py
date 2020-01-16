class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def generateCounts(word):
            curLetter = ""
            count = 0
            expressive = []
            for i in range(len(word)):
                if word[i] == curLetter:
                    count += 1
                elif curLetter != "":
                    expressive.append((curLetter, count))
                    count = 1
                    curLetter = word[i]
                else:
                    curLetter = word[i]
                    count += 1
            expressive.append((curLetter, count))
            return expressive
            
        SCount = generateCounts(S)    
        
        totCount = 0
        
        for word in words:
            wordCount = generateCounts(word)
            if len(wordCount) != len(SCount):
                continue
            flag = True
            for i in range(len(wordCount)):
                if SCount[i][0] != wordCount[i][0] or ( SCount[i][1] < 3 and SCount[i][1] != wordCount[i][1]) or SCount[i][1] < wordCount[i][1]:
                    flag = False
                    break
            if flag:
                totCount += 1
        return totCount
        
        