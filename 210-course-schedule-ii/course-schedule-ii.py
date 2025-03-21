class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        ans = []

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visited = 0
        while queue:
            course = queue.popleft()
            visited += 1
            ans.append(course)
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if visited == numCourses:
            return ans
        else:
            return []
