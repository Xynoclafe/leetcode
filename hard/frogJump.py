from collections import deque
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        lastElem = stones[-1]
        stoneSet = set(stones)
        if stones[1] != 1:
            return False
        
        if len(stones) == 2:
            return True
        
        seen = set((0, 0))
        nextJumps = deque([(1, 1)])
        nextSet = deque()
        
        while nextJumps:
            stone, jump = nextJumps.popleft()
            for i in [-1, 0, 1]:
                if jump + i > 0:
                    nextStone = stone + jump + i
                    if nextStone == lastElem:
                        return True
                    if (nextStone, jump + i) not in seen and nextStone in stoneSet:
                        seen.add((nextStone, jump + i))
                        nextSet.append((nextStone, jump + i))
            
            if len(nextJumps) == 0:
                nextJumps = nextSet
                nextSet = deque()
        
        return False
            
