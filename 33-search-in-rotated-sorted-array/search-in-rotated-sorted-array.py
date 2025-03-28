class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # [4 5 6 7 0 1 2]
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # [6 7 0 1 2 4 5]
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1

