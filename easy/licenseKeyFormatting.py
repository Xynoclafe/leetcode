class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        returnList = []
        S = S.replace("-", "")
        length = len(S)
        
        firstSet = length % K
        
        curSet = ""
        flag = True
        
        for i in range(length):
            
            element = S[i].upper()
            curSet += element
            if flag and len(curSet) == firstSet:
                flag = False
                returnList.append(curSet)
                curSet = ""
            elif len(curSet) == K:
                returnList.append(curSet)
                curSet = ""
        
        return "-".join(block for block in returnList)