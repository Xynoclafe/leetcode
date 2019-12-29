class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, i, j, word, path):
            if board[i][j] == word[0]:
                path.add((i,j))
                if len(word) == 1:
                    return True
                left = right = up = down = False
                if i > 0 and (i - 1, j) not in path:
                    left = dfs(board, i - 1, j, word[1:], path.copy())
                if not left and j > 0 and (i, j - 1) not in path:
                    up = dfs(board, i, j - 1, word[1:], path.copy())
                if not left and not up and i < len(board) - 1 and (i + 1, j) not in path:
                    right = dfs(board, i + 1, j, word[1:], path.copy())
                if not left and not up and not right and j < len(board[0]) - 1 and (i, j + 1) not in path:
                    down = dfs(board, i, j + 1, word[1:], path.copy())
                return up or down or left or right
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ret = dfs(board, i, j, word, set({}))
                    if ret:
                        return True
        return False
