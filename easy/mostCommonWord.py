class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wordDict = {}
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace(";", " ")
        words = paragraph.split()
        maxCount = -1
        maxWord = ""
        for word in words:
            if word not in banned:
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
                if wordDict[word] > maxCount:
                    maxCount = wordDict[word]
                    maxWord = word
        return maxWord
