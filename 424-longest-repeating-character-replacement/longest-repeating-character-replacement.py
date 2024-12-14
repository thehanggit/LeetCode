class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        c_frequency = {}
        longest_string = 0
        for right in range(len(s)):
            if s[right] not in c_frequency:
                c_frequency[s[right]] = 0
            
            c_frequency[s[right]] += 1
            cells_count =  right - left + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_string = max(longest_string, cells_count)
            
            else:
                c_frequency[s[left]] -= 1
                if not c_frequency:
                    c_frequency.pop(s[left])
                left += 1
        return longest_string