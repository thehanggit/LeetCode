class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # for each letter, we can record their position, or find their "window"
        # the goal is to find distinct windows such that it covers the whole string
        
        # first generate a dict to store those min, max
        # first = collections.defaultdict(int)
        # last = collections.defaultdict(int)
        # for i in range(len(s)):
        #     if s[i] not in first:
        #         first[s[i]] = i + 1
        #         last[s[i]] = i + 1
        #     else:
        #         first[s[i]] = min(first[s[i]], i + 1)
        #         last[s[i]] = max(last[s[i]], i + 1)
        # ans = []
        # j = 0
        # while j != len(s):
        #     l = first[s[j]]
        #     r = last[s[j]]
        #     for key, value in last.items():
        #         if value > r and first[key] < l:
        #             r = value
        #     j = r 
        #     ans.append([r - l + 1])
        # return ans
        last = {ch: i for i, ch in enumerate(s)}  # last index of each character
        result = []
        start = end = 0
        
        for i, ch in enumerate(s):
            end = max(end, last[ch])  # extend the partition if needed
            if i == end:
                result.append(end - start + 1)
                start = i + 1  # start of the next partition
                
        return result