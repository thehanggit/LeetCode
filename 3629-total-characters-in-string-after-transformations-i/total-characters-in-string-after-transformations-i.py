class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # define a recursion formula:
        # f(i,c) represents the charactor in ith transformation;
        # then for c = 0, f(i,0) = f(i - 1, 25)
        # for c = 1, f(i,1) = f(i - 1, 0) + f(i - 1, 25)
        # for c >= 2, f(i, c) = f(i-1, c-1)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        
        for round in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = cnt[25] + cnt[0]
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
            
        ans = sum(cnt) % (10**9 + 7)
        return ans
                