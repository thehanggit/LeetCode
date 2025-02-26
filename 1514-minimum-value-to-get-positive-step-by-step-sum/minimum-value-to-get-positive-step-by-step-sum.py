class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minval = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            minval = min(curr, minval)
        
        return 1 - minval