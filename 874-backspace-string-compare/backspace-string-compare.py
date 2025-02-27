class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for c in s:
            if c == "#":
                if s_stack:
                    s_stack.pop()
                else:
                    continue
            else:
                s_stack.append(c)
        for c2 in t:
            if c2 == "#":
                if t_stack:
                    t_stack.pop()
                else:
                    continue
            else:
                t_stack.append(c2)
        return "".join(s_stack) == "".join(t_stack)