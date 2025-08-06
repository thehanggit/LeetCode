class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        constraint = 1
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                constraint -= 1
                if constraint < 0:
                    return False
                if i - 1 > 0:
                    if nums[i - 2] >= nums[i]:
                        nums[i] = nums[i - 1]
        return True