class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s) - 1
        # skip the trailing spaces
        while right >= 0 and s[right] == " ":
            right -= 1
        left = right
        res = []
        while left >= 0:
            if s[left] == " ":
                if left < right:
                    res.append(s[left+1:right+1])
                while left >= 0 and s[left] == " ":
                    left -= 1
                right  = left
            else:
                left -= 1
        if right >= 0:
            res.append(s[0:right+1])
        return " ".join(res)
                    