class Solution:
    def numDecodings(self, s: str) -> int:
        # define do(i) as number of decoding ways with suffixs[i:]
        memo = {}
        n = len(s)
        def dp(i):
            if i == n:
                return 1
            if  s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i + 1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                memo[i] += dp(i + 2)
                
            return memo[i]
        return dp(0)