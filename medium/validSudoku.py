from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRowsandColumns(board):
            for i in range(9):
                repeatsRow = defaultdict(lambda: False)
                repeatsColumn = defaultdict(lambda: False)
                for j in range(9):
                    if board[i][j].isalnum():
                        if repeatsRow[board[i][j]] == False:
                            repeatsRow[board[i][j]] = True
                        else:
                            return False
                    if board[j][i].isalnum():
                        if repeatsColumn[board[j][i]] == False:
                            repeatsColumn[board[j][i]] = True
                        else:
                            return False
                    
                    if i in [0, 3, 6] and j in [0, 3, 6]:
                        repeats = defaultdict(lambda: False)
                        for x in range(3):
                            for y in range(3):
                                if board[i + x][j + y].isalnum():
                                    if not repeats[board[i + x][j + y]]:
                                        repeats[board[i + x][j + y]] = True
                                    else:
                                        return False
                    
            return True
        
        return checkRowsandColumns(board)