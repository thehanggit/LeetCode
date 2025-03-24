class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def backtrack(curr, i):
            if i == n:
                res.append(curr)
                return

            last_digit = curr % 10
            next_digits = set([last_digit + k, last_digit - k])
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    backtrack(curr * 10 + next_digit, i + 1)
            
        for j in range(1, 10):
            backtrack(j, 1)

        return res
                    

        
                