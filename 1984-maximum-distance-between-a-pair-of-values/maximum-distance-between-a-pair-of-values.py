class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        if nums1[m-1] > nums2[0]:
            return 0
        def check(k):
            for i in range(m):
                j = i + k
                if j >= n:
                    break
                if nums1[i] <= nums2[j]:
                    return True
            
            return False
        
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right if right != -1 else 0