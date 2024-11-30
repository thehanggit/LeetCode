class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)     
        dp = [[float("inf")] * n for _ in range(n)]        
        dp[0][:] = matrix[0][:]
        
        for row in range(1, n):
            for col in range(n):
                dp[row][col] = min(dp[row - 1][col], dp[row - 1][col + 1] if col + 1 < n else float("inf"), dp[row - 1][col - 1] if col else float("inf")) + matrix[row][col]
        
        return min(dp[-1])
    
