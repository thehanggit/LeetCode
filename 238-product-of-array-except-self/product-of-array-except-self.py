class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # L, R, ans = [1] * n, [1] * n, [1] * n

        # for i in range(1, n):
        #     L[i] = nums[i - 1] * L[i - 1]
             
        # for j in range(n-1, 0, -1):
        #     R[j - 1] = nums[j] * R[j]

        # for m in range(n):
        #     ans[m] = L[m] * R[m]

        # return ans

        n =  len(nums)
        L, R, ans = [1]*n, [1]*n, [1]*n

        for i in range(1, n):
            L[i] = nums[i- 1]*L[i -1]

        for j in range(n-1, 0, -1):
            R[j - 1] = nums[j]*R[j]
        
        for m in range(n):
            ans[m] = L[m] * R[m]
        
        return ans