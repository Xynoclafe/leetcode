class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        maxm = 0
        
        def findGold(i, j, visited):
            if grid[i][j] == 0:
                return 0
            visited.add((i,j))
            left = right = up = down = 0
            if i > 0 and (i - 1, j) not in visited:
                left = findGold(i - 1, j, visited.copy())
            if j > 0 and (i, j - 1) not in visited:
                up = findGold(i, j - 1, visited.copy())
            if i < len(grid) - 1 and (i + 1, j) not in visited:
                right = findGold(i + 1, j, visited.copy())
            if j < len(grid[0]) - 1 and (i, j + 1) not in visited:
                down = findGold(i, j + 1, visited.copy())
            return max(up, down, left, right) + grid[i][j]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxm = max(maxm, findGold(i, j, set({})))
        
        return maxm
        