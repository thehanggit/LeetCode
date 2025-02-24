class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return 
        rows = len(board)
        cols = len(board[0])
        dirs = [(0 , 1), (0, -1), (1, 0), (-1, 0)]
        borders = []
        for i in range(rows):
            borders.append([i, 0])
            borders.append([i, cols - 1])
        for j in range(cols):
            borders.append([0, j])
            borders.append([rows - 1, j])
        def dfs(x, y):
            if board[x][y] == "O":
                board[x][y] = "E"
                for dir in dirs:
                    if 0 < x + dir[0] < rows - 1 and 0 < y + dir[1] < cols - 1:
                        new_row = x + dir[0]
                        new_col = y + dir[1]
                        dfs(new_row, new_col)


        for row, col in borders:
            dfs(row, col)

        for m in range(rows):
            for n in range(cols):
                if board[m][n] == "O":
                    board[m][n] = "X"
                elif board[m][n] == "E":
                    board[m][n] = "O"
