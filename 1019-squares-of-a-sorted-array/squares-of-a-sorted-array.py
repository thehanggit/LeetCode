class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        
        n = len(nums)
        right = n - 1
        ans = [0] * n
        for i in range(n-1, -1, -1):
            p1 = nums[left] ** 2
            p2 = nums[right] ** 2
            if p1 < p2:
                ans[i] = p2
                right -= 1
            else:
                ans[i] = p1
                left += 1
        return ans