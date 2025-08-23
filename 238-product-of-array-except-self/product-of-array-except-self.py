class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n =  len(nums)
        L, R, ans = [1]*n, [1]*n, [1]*n
        for i in range(1, n):
            L[i] = L[i - 1]*nums[i-1]

        for j in range(n-1, 0, -1):
            R[j - 1] = R[j]*nums[j]
        
        for m in range(n):
            ans[m] = L[m]*R[m]
        return ans
