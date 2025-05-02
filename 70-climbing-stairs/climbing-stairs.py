class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        # def dp(i):
        #     if i == 0:
        #         return 1
        #     if i == 1:
        #         return 1
            
        #     return dp(i - 1) + dp(i - 2)
        # return dp(n)
        memo = {}
        def dp(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        return dp(n)