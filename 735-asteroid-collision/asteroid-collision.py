class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        stack = []
        for x in asteroids:
            while stack and x < 0 < stack[-1]:
                if -x > stack[-1]:
                    stack.pop()
                    continue
                elif -x == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(x)
        return stack