class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def getPerm(substring):
            index = -1
            listOfStrings = []
            for i in range(len(substring)):
                if substring[i] not in ["1", "2" ,"3", "4", "5", "6", "7", "8", "9", "0"]:
                    listOfStrings = getPerm(substring[i+1:])
                    index = i
                    break
            numStrings = len(listOfStrings)
            returnList = []
            for i in range(numStrings):
                returnList.append(substring[:index] + substring[index] + listOfStrings[i])
                returnList.append(substring[:index] + substring[index].swapcase() + listOfStrings[i])
            if len(returnList) == 0:
                returnList.append(substring)
            return returnList
        
        return getPerm(S)
