from math import floor
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                sum = 0
                if(j - 1 >= 0 and i - 1 >= 0):
                    sum += floor(board[i-1][j-1])
                if(j + 1 < len(board[0]) and i + 1 < len(board)):
                    sum += floor(board[i+1][j+1])
                if(j - 1 >= 0 and i + 1 < len(board)):
                    sum += floor(board[i+1][j-1])
                if(j + 1 < len(board[0]) and i - 1 >= 0):
                    sum += floor(board[i-1][j+1])
                if(j - 1 >= 0):
                    sum += floor(board[i][j-1])
                if(i - 1 >= 0):
                    sum += floor(board[i-1][j])
                if(j + 1 < len(board[0])):
                    sum += floor(board[i][j+1])
                if(i + 1 < len(board)):
                    sum += floor(board[i+1][j])
                print(board[i][j], sum)
                if(sum < 2 and board[i][j] == 1):
                    board[i][j] = 1.0
                elif((sum == 2 or sum == 3) and board[i][j] == 1):
                    board[i][j] = 1.1
                elif(sum > 3 and board[i][j] == 1):
                    board[i][j] = 1.0
                elif(sum == 3 and board[i][j] == 0):
                    board[i][j] = 0.1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 1.0):
                    board[i][j] = 0
                elif(board[i][j] == 1.1 or board[i][j] == 0.1):
                    board[i][j] = 1
