class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        #build prefix
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        #define binary search
        def binary_search(arr, target):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        ans = []
        for query in queries:
            i = binary_search(nums, query)
            ans.append(i)

        return ans
            