class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i != 0 and j != 0:
                        if matrix[0][j] != 0.7:
                            matrix[0][j] = 0.5
                        if matrix[i][0] != 0.7:
                            matrix[i][0] = 0.5
                    elif i == 0 and j == 0:
                        matrix[i][j] = 0.7
                    elif i == 0:
                        if matrix[i][0] != 0.7:
                            matrix[i][0] = 0.5
                        matrix[i][j] = 0.7
                    elif j == 0:
                        if matrix[0][j] != 0.7:
                            matrix[0][j] = 0.5
                        matrix[i][j] = 0.7
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0.5 or matrix[i][0] == 0.7:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0.5 or matrix[0][j] == 0.7:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
                    

        
        for i in range(len(matrix)):
            if matrix[i][0] == 0.5:
                matrix[i][0] = 0
            
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0.5:
                matrix[0][j] = 0
                
        for i in range(len(matrix)):
            if matrix[i][0] == 0.7:
                for j in range(len(matrix)):
                    if j != 0:
                        matrix[j][0] = 0
                break
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0.7:
                for i in range(len(matrix[0])):
                    if i != 0:
                        matrix[0][i] = 0
                break
        
        if matrix[0][0] == 0.7:
            matrix[0][0] = 0