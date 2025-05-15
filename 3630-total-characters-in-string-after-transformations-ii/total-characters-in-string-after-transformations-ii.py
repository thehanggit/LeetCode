class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # # brute force solution
        # cur = [0]*26
        # mod = 10**9 + 7
        # for ch in s:
        #     cur[ord(ch) - ord("a")] += 1
        # for round in range(t):
        #     nxt = [0]*26
        #     for j, cnt in enumerate(cur):
        #         if cnt == 0:
        #             continue
                
        #         transform = nums[j]
        #         for consec in range(1, transform + 1):
        #             k = (j + consec) % 26
        #             nxt[k] = (nxt[k] + cnt) % mod
            
        #     cur =  nxt
        # ans = sum(cur) % mod
        # return ans

        # matrix exponentiation
        mod = 10**9 + 7
        cur = [0]*26
        for ch in s:
            cur[ord(ch) - ord("a")] += 1

        # build transition matrix
        T = [[0]*26 for _ in range(26)]
        for i in range(26):
            for step in range(1, nums[i]+1):
                j = (i + step)%26
                T[j][i] += 1
        
        #matrix multiplication & fast power
        def mat_mul(A, B):
            C = [[0]* 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(26):
                            C[i][j] = (C[i][j] + aik * B[k][j]) % mod
            return C
        
        def mat_pow(A, exp):
            I = [[1 if i==j else 0 for j in range(26)] for i in range(26)]
            while exp:
                if exp & 1:
                    I = mat_mul(A, I)
                A = mat_mul(A, A)
                exp //= 2
            return I
        
        Tt = mat_pow(T, t)

        new = [0]*26
        for i in range(26):
            total = 0
            for j in range(26):
                total = (total + Tt[i][j] * cur[j]) % mod
            new[i] = total
        
        return sum(new) % mod

