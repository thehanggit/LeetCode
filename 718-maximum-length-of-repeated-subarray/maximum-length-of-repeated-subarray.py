class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # define dp(i, j) as maximum length of a subarray that appears in both arrays
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
               if nums1[i] == nums2[j]:
                dp[i][j] = dp[i+1][j+1] + 1
        return max(max(row) for row in dp)