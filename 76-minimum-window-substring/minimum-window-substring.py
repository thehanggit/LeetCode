class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        dict_t = defaultdict(int)
        for ch in t:
            dict_t[ch] += 1
        
        required = len(dict_t)
        left = 0
        dict_s = defaultdict(int)
        formed = 0
        res,ans =[-1,-1], float("infinity")

        for right in range(len(s)):
            ch = s[right]
            dict_s[ch] += 1

            if ch in dict_t and dict_t[ch] == dict_s[ch]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < ans:
                    res = [left, right]
                    ans = right - left + 1

                dict_s[s[left]] -= 1
                if s[left] in dict_t and dict_s[s[left]] < dict_t[s[left]]:
                    formed -= 1
                left += 1

        return s[res[0]:res[1] + 1] if ans != float("infinity") else ""

        
        