class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        directions = [[0,-1], [1, 0], [0, 1], [-1, 0]]
        visited = set({})
        
        def isValid(cell):
            return True if cell[0] in range(len(image)) and cell[1] in range(len(image[0])) else False
        
        def dfs(r, c, color, newColor):
            if color != image[r][c]:
                return
            visited.add((r,c))
            image[r][c] = newColor
            for x, y in directions:
                newCell = (r + x, c + y)
                if isValid(newCell) and newCell not in visited:
                    dfs(r + x, c + y, color, newColor)
        
        color = image[sr][sc]
        if color == newColor:
            return image
        else:
            dfs(sr, sc, color, newColor)
            return image
