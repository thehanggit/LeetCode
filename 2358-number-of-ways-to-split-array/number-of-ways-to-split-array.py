class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        ans = 0
        for i in range(len(nums) - 1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                ans += 1
        return ans