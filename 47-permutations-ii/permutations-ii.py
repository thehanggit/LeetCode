class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr, i, seen):
            if i == len(nums) and curr not in res:
                res.append(curr.copy())
                return
            
            for j in range(len(nums)):
                if j not in seen:
                    curr.append(nums[j])
                    seen.add(j)
                    backtrack(curr, i + 1, seen)
                    curr.pop()
                    seen.remove(j)
        
        backtrack([], 0, set())
        return res