class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        # define dp(i, holding) as maximum profit at day i
        def dp(i, holding):
            if i == len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            donothing = dp(i+1, holding)
            dosth = 0
            if holding:
                dosth = max(dosth, prices[i] + dp(i+1, 0) - fee)
            else:
                dosth = max(dosth, -prices[i] + dp(i+1, 1))
            memo[(i, holding)] = max(donothing, dosth)
            
            return memo[(i, holding)]
        return dp(0, 0)