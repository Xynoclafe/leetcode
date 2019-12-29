class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        code = {}
        code['2'] = ["a", "b", "c"]
        code['3'] = ["d", "e", "f"]
        code['4'] = ["g", "h", "i"]
        code['5'] = ["j", "k", "l"]
        code['6'] = ["m", "n", "o"]
        code['7'] = ["p", "q", "r", "s"]
        code['8'] = ["t", "u", "v"]
        code['9'] = ["w", "x", "y", "z"]
        
        returnList = set({})
        for char in digits:
            if len(returnList) == 0:
                returnList = set(code[char].copy())
            else:
                newList = set({})
                for item in returnList:
                    for alpha in code[char]:
                        newList.add(item + alpha)
                returnList = newList
        
        return list(returnList)
        
        
