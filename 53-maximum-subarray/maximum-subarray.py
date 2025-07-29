class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # currentsubarray = maxsubarray = nums[0]

        # for num in nums[1:]:
        #     currentsubarray = max(num, currentsubarray + num)
        #     maxsubarray = max(currentsubarray, maxsubarray)

        # return maxsubarray

        # best = current =  float('-inf')
        # for num in nums:
        #     current =  max(num, current + num)
        #     best = max(best, current)
        
        # return best
        res = current = float('-inf')
        for num in nums:
            current = max(num, num + current)
            res = max(res, current)
        return res