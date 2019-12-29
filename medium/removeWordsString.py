class Solution:
    def reverseWords(self, s: str) -> str:
        strArray = s.split(" ")
        retStr = ""
        for i in range(1, len(strArray) + 1):
            if(strArray[-i] != ""):
                print(strArray[-i])
                retStr += strArray[-i] + " "
        return retStr[:-1]
        
