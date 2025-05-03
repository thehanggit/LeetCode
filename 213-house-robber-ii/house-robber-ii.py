class Solution:
    def rob(self, nums: List[int]) -> int:
        # def sub_rob(sub_nums):
        #     if not sub_nums:
        #         return 0

        #     if len(sub_nums) == 1:
        #         return sub_nums[0]
            
        #     dp = [0]*len(sub_nums)
        #     dp[0] = sub_nums[0]
        #     if len(sub_nums) > 1:
        #         dp[1] = max(sub_nums[0], sub_nums[1])
            
        #     for i in range(2, len(sub_nums)):
        #         dp[i] = max(dp[i - 1], sub_nums[i] + dp[i - 2])
        #     return dp[-1]
            
        # if not nums:
        #     return 0
        # n = len(nums)
        # if n == 1:
        #     return nums[0]

        # return max(sub_rob(nums[1:]), sub_rob(nums[:-1]))
        def rob(sub_nums):
            if len(sub_nums) == 1:
                return sub_nums[0]
            dp = [0]*len(sub_nums)
            dp[0] = sub_nums[0]
            if len(sub_nums) > 1:
                dp[1] = max(dp[0], sub_nums[1])
            for i in range(2, len(sub_nums)):
                dp[i] = max(dp[i-1], dp[i-2] + sub_nums[i])
            return dp[-1]
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob(nums[1:]), rob(nums[:-1]))
        