class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])


        def dfs(u, v, visited):
            if u in adj[v]:
                return True
            for neighbor in adj[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(u, neighbor, visited):
                        return True
            return False
        
        ans = []
        for u, v in queries:
            ans.append(dfs(u, v, set()))
        return ans