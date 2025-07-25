class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        # define dp(i, j) as the min total cost for house at index i
        # recursion: dp(i, j) = min(i-1, k) for k not equal to j
        def dp(i, j):
            if i < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            best = float("inf")
            for k in range(3):
                if k != j:
                    best = min(best, dp(i-1, k))
            
            memo[(i, j)] = best + costs[i][j]
            return memo[(i, j)]
            
        ans = float("inf")
        for m in range(3):
            ans = min(dp(len(costs)-1, m), ans)
        return ans
            