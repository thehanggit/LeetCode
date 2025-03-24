class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def backtrack(curr, i, seen):
            if i == len(word):
                return True
            
            row, col = curr

            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1] 
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in seen and board[new_row][new_col] == word[i]:
                    seen.add((new_row, new_col))
                    if backtrack([new_row, new_col], i + 1, seen):
                        return True
                    seen.remove((new_row, new_col))
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] ==  word[0]:
                    if backtrack([i,j], 1, {(i, j)}):
                        return True
        
        return False
                    