class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfs(grid, i, j, scores):
            l1 = [[i,j]]
            l2 = []
            scores[i][j] = 0
            curScore = 0
            while(len(l1) > 0):
                indices = l1.pop(0)
                curVal = grid[indices[0]][indices[1]]
                x = indices[0]
                y = indices[1]
                if curVal == 0:
                    scores[x][y] = -1
                elif curVal == 1:
                    if scores[x][y] == -1 or scores[x][y] > curScore:
                        scores[x][y] = curScore
                        if x > 0:
                            l2.append([x - 1, y])
                        if x < len(grid) - 1:
                            l2.append([x + 1, y])
                        if y > 0:
                            l2.append([x, y - 1])
                        if y < len(grid[0]) - 1:
                            l2.append([x, y + 1])
                        
                elif curVal == -2 and i == x and j == y:
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
            return scores
        
        
        scores = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxScore = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = -2
                    scores = bfs(grid, i, j, scores)
        
        print(scores)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if maxScore < scores[i][j]:
                    maxScore = scores[i][j]
                if grid[i][j] == 1:
                    if scores[i][j] == -1:
                        return -1

        return maxScore
