from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.newList = [[0 for _ in range(n)] for _ in range(n)]
        self.colSum = [0 for _ in range(n)]
        self.rowSum = [0 for _ in range(n)]
        self.diag = 0
        self.revDiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.newList[row][col] = 1
            self.colSum[col] += 1
            self.rowSum[row] += 1
            if row == col:
                self.diag += 1
            if row + col == (self.n - 1):
                self.revDiag += 1
            if self.rowSum[row] == self.n or self.colSum[col] == self.n or self.diag == self.n or self.revDiag == self.n:
                return 1
        if player == 2:
            self.newList[row][col] = -1
            self.colSum[col] -= 1
            self.rowSum[row] -= 1
            if row == col:
                self.diag -= 1
            if row + col == (self.n - 1):
                self.revDiag -= 1
            if self.rowSum[row] == -self.n or self.colSum[col] == -self.n or self.diag == -self.n or self.revDiag == -self.n:
                return 2
        
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
