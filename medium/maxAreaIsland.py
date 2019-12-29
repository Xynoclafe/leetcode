class Solution:
    def area(self, grid, i, j):
        area = 0
        if(grid[i][j] == 1):
            area += 1
            grid[i][j] = -1
            if(i - 1 >= 0):
                area += self.area(grid, i - 1, j)
            if(j - 1 >= 0):
                area += self.area(grid, i, j - 1)
            if(i + 1 < len(grid)):
                area += self.area(grid, i + 1, j)
            if(j + 1 < len(grid[0])):
                area += self.area(grid, i, j + 1)
        return area
            
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    ar = self.area(grid, i, j)
                    maxArea = max(maxArea, ar)
        return maxArea
        
