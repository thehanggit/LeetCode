class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def dp(i):
        #     ans = 1
            
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             ans = max(dp(j) + 1, ans)
            
        #     return ans
        
        # memo = {}
        # for i in range(len(nums)):
        #     memo[i] = dp(i)
        
        # return memo[len(nums) - 1]
        memo = {}
        def dp(i):
            if i == 0:
                return 1
            if i in memo:
                return memo[i]
                
            best = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    best = max(dp(j) + 1, best)
            memo[i] = best
            return memo[i]

        return max(dp(i) for i in range(len(nums)))