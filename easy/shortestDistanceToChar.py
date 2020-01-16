class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        returnList = [0] * len(S)
        locations = []
        for i in range(len(S)):
            if S[i] == C:
                locations.append(i)
        
        j = 0
        occurences = len(locations)
        for i in range(len(S)):
            if j == occurences - 1:
                returnList[i] = abs(locations[j] - i)
            else:
                x = abs(locations[j] - i)
                y = abs(locations[j + 1] - i)
                if x < y:
                    returnList[i] = x
                else:
                    returnList[i] = y
                    j += 1
        return returnList