class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0
        
        # for i in range(amount + 1):
        #     for coin in coins:
        #         if i - coin >= 0:
        #             dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # return dp[amount] if dp[amount] != (amount + 1) else -1
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            
            best = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    best = min(best, dp(i - coin) + 1)
            memo[i] = best
            return memo[i]

        return dp(amount)  if dp(amount) != float("inf") else -1

             