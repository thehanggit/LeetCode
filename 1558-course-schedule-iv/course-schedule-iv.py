class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])

        memo = {}

        def dfs(u, v):
            if (u, v) in memo:
                return memo[(u, v)]
            if u in adj[v]:
                memo[(u, v)] = True
                return True
            for neighbor in adj[v]:
                if dfs(u, neighbor):
                    memo[(u, v)] = True
                    return True
            memo[(u, v)] =  False
            return False
        
        return [dfs(u, v) for u, v in queries]