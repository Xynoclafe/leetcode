class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        nRows = len(matrix)
        if nRows == 0:
            return []
        nColumns = len(matrix[0])
        
        returnList = []
        i = 0
        j = 0
        while(nRows > 0 and nColumns > 0):
            for _ in range(nColumns):
                returnList.append(matrix[i][j])
                j += 1
            nRows -= 1
            j -= 1
            i += 1
            
            if nRows == 0 or nColumns == 0:
                break
            
            for _ in range(nRows):
                returnList.append(matrix[i][j])
                i += 1
            nColumns -= 1
            i -= 1
            j -= 1
            
            if nRows == 0 or nColumns == 0:
                break
            
            for _ in range(nColumns):
                returnList.append(matrix[i][j])
                j -= 1
            nRows -= 1
            j += 1
            i -= 1
            
            if nRows == 0 or nColumns == 0:
                break
            
            for _ in range(nRows):
                returnList.append(matrix[i][j])
                i -= 1
            nColumns -= 1
            i += 1
            j += 1
        return returnList