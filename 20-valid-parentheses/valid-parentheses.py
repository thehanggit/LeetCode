class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(":")", "[":"]", "{":"}"}

        for ch in s:
            if ch in matching:
                stack.append(ch)
            else:
                if stack == []:
                    return False
                
                last_paretheses = stack.pop()
                if matching[last_paretheses] != ch:
                    return False
        
        return not stack
                    