class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # lets first think about how many variables we can have
        # remain should be stopping criteria, which relates to target
        # lets think about it carefully, if for houses [a, b, c, d], the non-zero values could be figured out and lower bound of neighborhoods are clear
        @cache
        def dp(i, j, group):
            if i == len(cost) and group == target:
                return 0
            if i >= len(cost):
                return float("inf")
            if group > target:
                return float("inf")
            
            res = float("inf")
            if not houses[i]:
                for color in range(1, n + 1):
                    if j != color:
                        res = min(res, dp(i + 1, color, group + 1) + cost[i][color - 1])
                    else:
                        res = min(res, dp(i + 1, color, group) + cost[i][color - 1])

            else:
                color = houses[i]
                res = dp(i + 1, color, group + 1) if j != color else dp(i + 1, color, group)
            
            return res
        
        res = dp(0, -1, 0)
        return -1 if res == float("inf") else res