class Solution:
    def findLands(self, grid, i, j, count):
        if(grid[i][j] == "1"):
            grid[i][j] = str(count)
            if(i < len(grid) - 1):
                self.findLands(grid, i+1, j, count)
            if(j < len(grid[0]) - 1):
                self.findLands(grid, i, j+1, count)
            if(j > 0):
                self.findLands(grid, i, j-1, count)
            if(i > 0):
                self.findLands(grid, i-1, j, count)
        return
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    self.findLands(grid, i, j, -count)
                    count += 1
        print(grid)
        return count - 1
