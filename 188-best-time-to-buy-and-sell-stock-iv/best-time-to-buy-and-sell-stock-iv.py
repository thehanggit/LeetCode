class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # dp(time, hold, remain)
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]
        for day in range(n -1, -1, -1):
            for holding in range(2):
                for remain in range(1, k + 1):
                    ans = dp[day + 1][holding][remain]
                    if holding:
                        ans = max(ans, prices[day] + dp[day + 1][0][remain - 1])
                    else:
                        ans = max(ans, -prices[day] + dp[day + 1][1][remain])
                    dp[day][holding][remain] = ans

        return dp[0][0][k]
        # n = len(prices)
        # memo = {}
        # def dp(i, trans_remain, holding):
        #     if trans_remain == 0 or i == len(prices):
        #         return 0
            
        #     if (i, trans_remain, holding) in memo:
        #         return memo[(i, trans_remain, holding)]
            
        #     # construct options
        #     donothing = dp(i+1, trans_remain, holding)
        #     if holding == 1:
        #         memo[(i, trans_remain, holding)] = max(donothing, prices[i] + dp(i + 1, trans_remain-1, 0))
        #     else:
        #         memo[(i, trans_remain, holding)] = max(donothing, -prices[i] + dp(i + 1, trans_remain, 1))
        #     return memo[(i, trans_remain, holding)]

        # return dp(0, k, 0)
                        