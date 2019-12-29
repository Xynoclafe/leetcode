class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(grid, i, j):
            l1 = [[i,j]]
            l2 = []
            curScore = grid[i][j]
            while(len(l1) > 0):
                indices = l1.pop(0)
                curVal = grid[indices[0]][indices[1]]
                x = indices[0]
                y = indices[1]
                if curVal == -1:
                    grid[x][y] = curVal
                elif curVal == 0 and x == i and y == j:
                    if x > 0:
                        l2.append([x - 1, y])
                    if x < len(grid) - 1:
                        l2.append([x + 1, y])
                    if y > 0:
                        l2.append([x, y - 1])
                    if y < len(grid[0]) - 1:
                        l2.append([x, y + 1])
                else:
                    if grid[x][y] > curScore:
                        grid[x][y] = curScore
                        if x > 0:
                            l2.append([x - 1, y])
                        if x < len(grid) - 1:
                            l2.append([x + 1, y])
                        if y > 0:
                            l2.append([x, y - 1])
                        if y < len(grid[0]) - 1:
                            l2.append([x, y + 1])
                            
                if(len(l1) == 0):
                    curScore += 1
                    l1 = l2
                    l2 = []
            
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    bfs(rooms, i, j)
        
        print(rooms)
        
