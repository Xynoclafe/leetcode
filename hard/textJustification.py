class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        runningLength = 0
        noSpaceLength = 0
        wordGroups = []
        curList = []
        
        def createString(wordList, length, lastLine):
            totLength = len(wordList) - 1
            outString = ""
            outString += wordList.pop(0)
            if len(wordList) == 0:
                outString += (" " * (maxWidth - length))
                return outString
            if lastLine:
                while len(wordList) > 0:
                    outString += " "
                    outString += wordList.pop(0)
                outString += (" " * (maxWidth - len(outString)))
                return outString
            if (maxWidth - length) % totLength == 0:
                space = (maxWidth - length) // totLength
                while len(wordList) > 0:
                    outString += (" " * space)
                    outString += wordList.pop(0)
                return outString
            else:
                spaces = []
                for i in range(totLength):
                    if (maxWidth - length - i) % totLength != 0:
                        spaces.append(1)
                    else:
                        break
                        
                space = (maxWidth - length) // totLength
                count = 0
                while len(wordList) > 0:
                    if count < len(spaces):
                        outString += (" " * (space + 1))
                    else:
                        outString += (" " * space)
                    outString += wordList.pop(0)
                    count += 1
                return outString
        
        for word in words:
            if runningLength + len(word) <= maxWidth:
                curList.append(word)
                runningLength += len(word) + 1
                noSpaceLength += len(word)
            else:
                wordGroups.append(createString(curList, noSpaceLength, False))
                curList = [word]
                runningLength = len(word) + 1
                noSpaceLength = len(word)
                
        if curList:
            wordGroups.append(createString(curList, noSpaceLength, True))
        return wordGroups
