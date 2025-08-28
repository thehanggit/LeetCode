class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # intuition use 2D dp to check with memorization
        # not a good option using two pointers because of try&error
        if len(s1) + len(s2) != len(s3):
            return False
        memo  = {}
        def dp(i, j):
            #base case
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            k = i + j
            ans = False
            if i < len(s1) and s1[i] == s3[k] and dp(i + 1, j):
                return True
            elif j < len(s2) and s2[j] == s3[k] and dp(i, j + 1):
                return True
            
            memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0, 0)