class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def solve(string, pattern, score):
            stack = []
            points = 0
            for c in string:
                if stack and stack[-1] == pattern[0] and c == pattern[1]:
                    stack.pop()
                    points += score
                else:
                    stack.append(c)
            return points, "".join(stack)

        if x > y:
            points1, remain = solve(s, "ab", x)
            points2, _ = solve(remain, "ba", y)
        else:
            points1, remain = solve(s, "ba", y)
            points2, _ = solve(remain, "ab", x)
        
        return points1 + points2

    
