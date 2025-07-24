class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # words = set(wordDict)
        # queue = deque([0])
        # seen = set()

        # while queue:
        #     start = queue.popleft()
        #     if start == len(s):
        #         return True
            
        #     for end in range(start + 1, len(s) + 1):
        #         if end in seen:
        #             continue
                
        #         if s[start:end] in words:
        #             queue.append(end)
        #             seen.add(end)
        # return False

        # try dynamic programming
        memo = {}
        def dp(i):
            if i < 0:
                return True
            if i in memo:
                return memo[i]
            memo[i] = False
            for word in wordDict:
                if (i >= len(word) - 1) and dp(i - len(word)):
                    if s[i - len(word) + 1: i + 1] == word:
                        memo[i] = True
            return memo[i]
        return dp(len(s) - 1)
        