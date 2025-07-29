class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy method: first, we generate an array for all indices with true that can reach last element
        # then we perform largest steps to true indices from 0 index
        n = len(nums)
        feasible_array = [False] * n
        feasible_array[-1] = True
        goal = n - 1
        for i in range(goal, -1, -1):
            if i + nums[i] >= goal:
                feasible_array[goal] = True
                goal = i
        
        # imagine u have found out all feasible positions that can reach last element with T/F, then we can perform dp to solve the minimization problem
        memo = {}
        def dp(i):
            if i >= n - 1:
                return 0

            if i in memo:
                return memo[i]
            
            res = float("inf")
            for j in range(1, nums[i] + 1):

                if i + j < n and feasible_array[i + j]:
                    res = min(dp(i + j), res)
            
            memo[i] = res + 1
            return memo[i]
        return dp(0)
        
