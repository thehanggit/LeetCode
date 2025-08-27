class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            nums = set(nums)
            if i not in nums:
                return i