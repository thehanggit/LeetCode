class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] = 1
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1 or (row, col) == (0, 0):
                    continue
                dp[row][col] = (dp[row - 1][col] if row else 0) + (dp[row][col - 1] if col else 0)
                
        if obstacleGrid[0][0] == 1:
            return 0
        
        return dp[rows - 1][cols - 1]

