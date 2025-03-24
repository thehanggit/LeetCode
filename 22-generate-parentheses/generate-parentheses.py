class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res = []
        # def backtrack(subset, left_count, right_count):
        #     if len(subset)/2 == n:
        #         res.append("".join(subset))
                
        #     if left_count < n:
        #         subset.append("(")
        #         backtrack(subset, left_count + 1, right_count)
        #         subset.pop()
        #     if right_count < left_count:
        #         subset.append(")")
        #         backtrack(subset, left_count, right_count + 1)
        #         subset.pop()
            
        # backtrack([], 0, 0)
        # return res

        res = []
        def backtrack(subset, left_count, right_count):
            if len(subset) // 2 == n:
                res.append("".join(subset.copy()))
            
            if left_count < n:
                subset.append("(")
                backtrack(subset, left_count + 1, right_count)
                subset.pop()

            if right_count < left_count:
                subset.append(")")
                backtrack(subset, left_count, right_count + 1)
                subset.pop()
            
        backtrack([], 0, 0)
        return res