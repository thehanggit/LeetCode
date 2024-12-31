class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []  # Separate stack for s
        stack_t = []  # Separate stack for t

        # Process the string s
        for ch in s:
            if ch == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(ch)

        # Process the string t
        for ch in t:
            if ch == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(ch)

        # Compare the final states of the two stacks
        return "".join(stack_s) == "".join(stack_t)