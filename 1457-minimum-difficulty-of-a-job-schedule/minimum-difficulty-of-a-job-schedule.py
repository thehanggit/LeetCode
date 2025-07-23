class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        # construct the dp problem
        # dp(i, day) = min(hardest + dp(j+1, day+1)) for i <= j <= n - (d - day)
        # hardest = max(jobDifficulty[k]) for i <= k <= j
        memo = {}
        def dp(i, day):
            # base case:
            if day == d:
                return max(jobDifficulty[i:])
            
            if (i, day) in memo:
                return memo[(i, day)]
            best = float("inf")
            hardest = 0
            for j in range(i, n - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1))
            memo[(i, day)] = best
            return best

        return dp(0, 1)