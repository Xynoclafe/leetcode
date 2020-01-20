from collections import defaultdict
from collections import deque
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        xCoordinate = defaultdict(lambda: deque([]))
        yCoordinate = defaultdict(lambda: deque([]))
        visited = set({})
        
        for stone in stones:
            xCoordinate[stone[0]].append(stone)
            yCoordinate[stone[1]].append(stone)

        def dfs(stone):
            visited.add(tuple(stone))
            count = 0
            for x in xCoordinate[stone[0]]:
                if tuple(x) not in visited:
                    count += dfs(x)
            
            for y in yCoordinate[stone[1]]:
                if tuple(y) not in visited:
                    count += dfs(y)
            
            count += 1
            return count
        
        count = 0
        for stone in stones:
            if tuple(stone) not in visited:
                count += dfs(stone)
                count -= 1
        
        return count
