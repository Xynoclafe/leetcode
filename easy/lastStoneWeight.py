import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negList = [-item for item in stones]
        heapq.heapify(negList)
        while(len(negList) > 1):
            y = -(heapq.heappop(negList))
            x = -(heapq.heappop(negList))
            if x != y:
                y -= x
                heapq.heappush(negList, -y)
        if len(negList) == 0:
            return 0
        else:
            return -negList[0]
