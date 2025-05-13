class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        zeros1 = 0
        for num in nums1:
            if num != 0:
                sum1 += num
            else:
                zeros1 += 1
        sum1 += zeros1
        
        sum2 = 0
        zeros2 = 0
        for num in nums2:
            if num != 0:
                sum2 += num
            else:
                zeros2 += 1
        sum2 += zeros2
        if sum1 == sum2:
            return sum1
        elif sum1 > sum2 and zeros2 != 0:
            return sum1
        elif sum2 > sum1 and zeros1 != 0:
            return sum2
        return -1