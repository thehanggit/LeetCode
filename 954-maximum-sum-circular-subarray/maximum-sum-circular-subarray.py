class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # you need to come up with a solution that in a circular way, it is max(total sum of array - minimum subarray)
        def max_kadane(arr: List[int]):
            current = 0
            best = float('-inf')
            for num in arr:
                current = max(num, current + num)
                best = max(current, best)
            return best

        def min_kadane(arr):
            current = 0
            best = float('inf')
            for num in arr:
                current = min(num, current + num)
                best = min(current, best)
            return best
        
        total = sum(nums)
        max_k = max_kadane(nums)
        min_k = min_kadane(nums)
        if max_k < 0:
            return max_k
        return max(max_k, total - min_k)