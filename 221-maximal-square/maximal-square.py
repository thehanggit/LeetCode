class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        max_side = 0
        def dp(i, j):
            nonlocal max_side
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i ,j)]
            
            if matrix[i][j] == "1":
                side = 1 + min(dp(i - 1, j), dp(i - 1, j - 1), dp(i, j - 1))
                memo[(i, j)] = side
                max_side = max(max_side, side)
            else:
                memo[(i, j)] = 0
            return memo[(i, j)]
        
        for i in range(rows):
            for j in range(cols):
                dp(i, j)
                
        return max_side * max_side