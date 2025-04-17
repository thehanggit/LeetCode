class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # def backtrack(i, curr, total):
        #     if total == target:
        #         res.append(curr.copy())
        #         return
            
        #     for j in range(i, len(candidates)):
        #         if total + candidates[j] <= target:
        #             curr.append(candidates[j])
        #             backtrack(j, curr, total + candidates[j])
        #             curr.pop()
        
        # backtrack(0, [], 0)
        # return res

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] <= target:
                    curr.append(candidates[j])
                    backtrack(j, curr, total + candidates[j])
                    curr.pop()
        
        backtrack(0, [], 0)
        return res