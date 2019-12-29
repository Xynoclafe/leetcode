class Solution:
    from math import sqrt
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        newList = []
        retList = []
        for item in points:
            newList.append([item[0]**2 + item[1]**2, item])
        newList.sort()
        for i in range(K):
            retList.append(newList[i][1])
        return retList
        
