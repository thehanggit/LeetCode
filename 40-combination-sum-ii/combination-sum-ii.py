class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                curr.append(candidates[j])
                backtrack(j + 1, curr, total + candidates[j])
                curr.pop()
        
        backtrack(0, [], 0)
        return res
            