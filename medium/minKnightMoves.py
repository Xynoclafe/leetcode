from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        directions = [(1, -2), (-1, -2), (2, 1), (2, -1), (-1, 2), (1, 2), (-2, 1), (-2, -1)]
        visited = set((0,0))
        
        if (0,0) == (x,y):
            return 0
        
        x = abs(x)
        y = abs(y)
        
        l1 = deque([(0,0)])
        l2 = deque([])
        moves = 0
        
        while len(l1) > 0:
            cell = l1.popleft()
            
            for direction in directions:
                newCell = (cell[0] + direction[0], cell[1] + direction[1])
                if newCell not in visited and newCell[0] > -3 and newCell[1] > -3:
                    if newCell == (x,y):
                        return moves + 1
                    l2.append(newCell)
                    visited.add(newCell)
            
            if len(l1) == 0:
                moves += 1
                l1 = l2
                l2 = deque([])
                
