class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        ans = 0
        curr = 0
        hashmap[0] = 1
        for num in nums:
            curr += num
            ans += hashmap[curr - k]
            hashmap[curr] += 1
        return ans
