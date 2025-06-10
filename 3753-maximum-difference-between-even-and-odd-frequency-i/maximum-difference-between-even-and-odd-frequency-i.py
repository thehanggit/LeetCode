class Solution:
    def maxDifference(self, s: str) -> int:
        max_freq = 0
        min_freq = float('inf')
        # frequencies = defaultdict(int)
        # for char in s:
        #     frequencies[char] += 1
        frequencies = Counter(s)
        for key, value in frequencies.items():
            if value % 2 == 0 and value < min_freq:
                min_freq = value
            elif value % 2 == 1 and value > max_freq:
                max_freq = value
        return max_freq - min_freq
    