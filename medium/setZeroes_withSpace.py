class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [False for _ in range(len(matrix))]
        column = [False for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    column[j] = True
        
        for i in range(len(row)):
            if row[i]:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(len(column)):
            if column[j]:
                for i in range(len(matrix)):
                    matrix[i][j] = 0