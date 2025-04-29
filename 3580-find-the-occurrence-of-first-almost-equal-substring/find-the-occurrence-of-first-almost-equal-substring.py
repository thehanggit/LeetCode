class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z
        n, m = len(s), len(pattern)
        z1 = z_function(pattern + s)
        z2 = z_function(pattern[::-1] + s[::-1])
        for i in range(n - m + 1):
            if z1[m + i] + 1 + z2[n - i] >= m:
                return i
        return -1

