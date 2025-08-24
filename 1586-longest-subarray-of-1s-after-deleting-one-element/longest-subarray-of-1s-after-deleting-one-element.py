class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        element = 1
        l =  ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                element -= 1
            while element < 0:
                if nums[l] == 0:
                    element += 1
                l += 1
            ans = max(ans, r - l)
        return ans