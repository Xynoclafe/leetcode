class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)
        commonSet = set1.intersection(set2)
        finalList = []
        curSum = 10 ** 10
        for item in commonSet:
            index1 = list1.index(item)
            index2 = list2.index(item)
            indexSum = index1 + index2
            if indexSum < curSum:
                finalList = []
                finalList.append(item)
                curSum = indexSum
            elif indexSum == curSum:
                finalList.append(item)
        return finalList
