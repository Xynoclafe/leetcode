from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        l1 = deque([start])
        l2 = deque()
        directions  = [[0,1], [1,0], [-1,0], [0,-1]]
        
        visited = set()
        visited.add(tuple(start))
        
        def findExtreme(position, direction):
            newPos = position
            while((0 <= newPos[0] < len(maze)) and (0 <= newPos[1] < len(maze[0]) and maze[newPos[0]][newPos[1]] != 1)):
                prevPos = newPos
                newPos = [newPos[0] + direction[0], newPos[1] + direction[1]]
            if tuple(prevPos) not in visited:
                return prevPos
            else:
                return None
            
        
        while l1:
            curPos = l1.popleft()
            for direction in directions:
                newPos = findExtreme(curPos, direction)
                if newPos:
                    if newPos == destination:
                        return True
                    l2.append(newPos)
                    visited.add(tuple(newPos))
            
            if len(l1) == 0:
                l1 = l2
                l2 = deque()
        
        return False
