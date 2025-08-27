class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = left = 0
        end = right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > start and nums[mid] < nums[mid - 1]:
                right = mid - 1
            elif mid < end and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid
        