class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # memo = {}
        # # define dp(i, j) as the min total cost for house at index i
        # # recursion: dp(i, j) = min(i-1, k) for k not equal to j
        # def dp(i, j):
        #     if i < 0:
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     best = float("inf")
        #     for k in range(3):
        #         if k != j:
        #             best = min(best, dp(i-1, k))
            
        #     memo[(i, j)] = best + costs[i][j]
        #     return memo[(i, j)]
            
        # ans = float("inf")
        # for m in range(3):
        #     ans = min(dp(len(costs)-1, m), ans)
        # return ans
        from functools import lru_cache

        n = len(costs)

        @lru_cache(maxsize=None)
        def dp(i: int):
            # returns a tuple: (min cost ending in color 0, color 1, color 2)
            if i < 0:
                return (0, 0, 0)

            prev = dp(i - 1)
            cost0 = costs[i][0] + min(prev[1], prev[2])
            cost1 = costs[i][1] + min(prev[0], prev[2])
            cost2 = costs[i][2] + min(prev[0], prev[1])

            return (cost0, cost1, cost2)

        return min(dp(n - 1))       