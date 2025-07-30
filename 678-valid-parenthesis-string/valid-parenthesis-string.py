class Solution:
    def checkValidString(self, s: str) -> bool:
        # previously we check it with a dict
        # now we only need one more logic, that is when the stack only has *, return true.
        # need dp?
        # use backtrack to record every possibility
        leftmin =  leftmax = 0
        for ch in s:
            if ch == "(":
                leftmin, leftmax = leftmin +1, leftmax +1
            elif ch == ")":
                leftmin, leftmax = leftmin-1, leftmax-1
            elif ch == "*":
                leftmin, leftmax = leftmin-1, leftmax+1
            
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0

        return leftmin == 0