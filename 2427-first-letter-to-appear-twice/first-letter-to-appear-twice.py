class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashmap = defaultdict(int)
        for ch in s:
            hashmap[ch] += 1
            if hashmap[ch] == 2:
                return ch
    