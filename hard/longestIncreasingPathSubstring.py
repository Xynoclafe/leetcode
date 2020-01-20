class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        directions = [(1,0), (-1, 0), (0,1), (0, -1)]
        seenPath = dict()
        
        def isValid(x,y, value):
            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
                if matrix[x][y] > value:
                    return True
            return False
            
        def longestPath(i,j):
            
            if (i,j) in seenPath:
                return seenPath[(i,j)]
            
            paths = [0]
            for x,y in directions:
                if isValid(i + x, j + y, matrix[i][j]):
                    paths.append(longestPath(i + x, j + y))
            
            seenPath[(i, j)] = max(paths) + 1
            return seenPath[(i,j)]
        
        curMax = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curMax = max(curMax, longestPath(i,j))
        
        return curMax
