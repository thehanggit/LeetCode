class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(curr, i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                backtrack(curr, j + 1)
                curr.pop()
        
        backtrack([], 1)
        return res