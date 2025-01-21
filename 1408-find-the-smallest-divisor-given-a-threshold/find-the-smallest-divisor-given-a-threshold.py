class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # def check(divisor):
        #     sum_divisor = 0
        #     for num in nums:
        #         sum_divisor += ceil(num/divisor)
        #     return sum_divisor <= threshold

        # left = 1
        # right = max(nums)
        # while left <= right:
        #     mid = (left + right) // 2
        #     if check(mid):
        #         right = mid - 1
        #     else:
        #         left = mid + 1
            
        # return left

        def check(k):
            result = 0
            for num in nums:
                result += ceil(num/k)
            return result <= threshold

        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left