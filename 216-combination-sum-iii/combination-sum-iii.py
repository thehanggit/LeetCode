class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # if k > n:
        #     return []
        
        # res = []
        # def backtrack(subset, i, last, remain):
        #     if i == k and remain == 0:
        #         res.append(subset[:])
        #         return
            
        #     for num in range(last + 1, 10):
        #         new_remain = remain - num
        #         if new_remain >= 0:
        #             subset.append(num)
        #             backtrack(subset, i + 1, num, new_remain)
        #             subset.pop()
                    
        # backtrack([], 0, 0, n)
        
        # return res

        if k > n:
            return []
        
        res = []
        
        def backtrack(subset, curr, i):
            if curr == n and i == k:
                res.append(subset.copy())
                return
            if subset:
                start = subset[-1] + 1
            else:
                start = 1
            for j in range(start, 10):
                if curr + j <= n:
                    subset.append(j)
                    backtrack(subset, curr + j, i + 1)
                    subset.pop()
            
        backtrack([], 0, 0)
        return res


            