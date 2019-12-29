class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(target, matrix, visited, i, j):
            curNum = matrix[i][j]
            visited[i][j] = True
            if curNum < target:
                row = False
                column = False
                if i < (len(matrix) - 1):
                    if not visited[i + 1][j]:
                        row = search(target, matrix, visited, i + 1, j)
                if j < (len(matrix[0]) - 1):
                    if not visited[i][j + 1]:
                        column = search(target, matrix, visited, i, j + 1)
                return (row or column)
            elif curNum == target:
                return True
            else:
                return False
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        return search(target, matrix, visited, 0, 0)
