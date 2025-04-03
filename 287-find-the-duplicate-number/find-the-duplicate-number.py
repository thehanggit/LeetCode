class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            if num in hashmap:
                return num
            else:
                hashmap[num] += 1
        