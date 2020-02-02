from collections import deque
from collections import defaultdict
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        l1 = deque([(start, 0)])
        l2 = deque()
        directions  = [[0,1], [1,0], [-1,0], [0,-1]]
        minJumps = float("inf")
        
        visited = defaultdict(lambda: float("inf"))
        visited[tuple(start)] = 0
        
        def findExtreme(position, direction, numJumps):
            newPos = position
            while((0 <= newPos[0] < len(maze)) and (0 <= newPos[1] < len(maze[0]) and maze[newPos[0]][newPos[1]] != 1)):
                prevPos = newPos
                newPos = [newPos[0] + direction[0], newPos[1] + direction[1]]
                numJumps += 1
            if visited[tuple(prevPos)] > (numJumps - 1):
                return prevPos, numJumps - 1
            else:
                return None
            
        
        while l1:
            curPos, jumps = l1.popleft()
            for direction in directions:
                retVal = findExtreme(curPos, direction, jumps)
                if retVal:
                    newPos = retVal[0]
                    numJumps = retVal[1]
                    l2.append((newPos, numJumps))
                    visited[tuple(newPos)] = numJumps
            
            if len(l1) == 0:
                l1 = l2
                l2 = deque()
                jumps += 1
        
        return visited[tuple(destination)] if visited[tuple(destination)] != float("inf") else -1
