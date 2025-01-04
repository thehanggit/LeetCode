class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = maxLen = 0
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            maxLen = max(maxLen, right - left + 1)
            substring.add(s[right])
        return maxLen