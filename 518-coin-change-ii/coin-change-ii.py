class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # i define the index of using ith coin, remain as remaining amount  
        memo = {}
        def dp(i, remain):
            if remain == 0:
                return 1
            if i ==  len(coins):
                return 0
            
            if (i, remain) in memo:
                return memo[(i, remain)]
            
            if coins[i] > remain:
                memo[(i, remain)] = dp(i + 1, remain)
            else:
                memo[(i, remain)] = dp(i, remain - coins[i]) + dp(i + 1, remain)
            return memo[(i, remain)]

        return dp(0, amount)