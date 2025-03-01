class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashmap = defaultdict(int)
        for arr in nums:
            for num in arr:
                hashmap[num] += 1
        
        ans = []
        for key, value in hashmap.items():
            if value == len(nums):
                ans.append(key)
        ans.sort()
        return ans