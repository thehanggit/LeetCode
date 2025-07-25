class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        total = 0
        max_neg = float("-inf")
        for num in nums:
            if num >= 0 and num not in seen:
               total += num
               seen.add(num)
            elif num < 0:
                max_neg = max(num, max_neg)
        return total if len(seen) > 0 else max_neg