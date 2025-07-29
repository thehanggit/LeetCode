class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i, ch in enumerate(s):
            hashmap[ch] = i
        size = end = 0
        ans = []
        for i, ch in enumerate(s):
            size += 1
            end = max(hashmap[ch], end)
            if end == i:
                ans.append(size)
                size = 0
        return ans
                