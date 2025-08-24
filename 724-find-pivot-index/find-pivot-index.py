class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        sums = sum(nums)
        left_total = 0
        for index in range(len(nums)):
            right_total = sums - left_total - nums[index]
            if left_total == right_total:
                return index
            left_total += nums[index]
        return -1