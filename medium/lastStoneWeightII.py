class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        stonesLeft = [stones[0], -stones[0]]
        for i in range(1, len(stones)):
            newList = set([])
            for stone in stonesLeft:
                newList.add(stone + stones[i])
                newList.add(stone - stones[i])
            stonesLeft = list(newList)
            
        heapq.heapify(stonesLeft)
        stone = heapq.heappop(stonesLeft)
        while(stone < 0):
            stone = heapq.heappop(stonesLeft)
        return stone