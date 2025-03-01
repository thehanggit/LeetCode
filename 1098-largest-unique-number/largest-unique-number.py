class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        uni_max = float("-inf")
        for num, fre in hashmap.items():
            if fre == 1:
                uni_max = max(num, uni_max)

        return (uni_max if uni_max != float("-inf") else -1)