class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # adj = [[] for _ in range(numCourses)]

        # for pre in prerequisites:
        #     adj[pre[1]].append(pre[0])


        # def dfs(u, v, visited):
        #     if u in adj[v]:
        #         return True
        #     for neighbor in adj[v]:
        #         if neighbor not in visited:
        #             visited.add(neighbor)
        #             if dfs(u, neighbor, visited):
        #                 return True
        #     return False
        
        # ans = []
        # for u, v in queries:
        #     ans.append(dfs(u, v, set()))
        # return ans

        # adj = [[] for _ in range(numCourses)]
        # indegree = [0] * numCourses

        # for pre in prerequisites:
        #     adj[pre[0]].append(pre[1])
        #     indegree[pre[1]] += 1

        # nodesprerequisites = defaultdict(set)
        # q = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)

        # while q:
        #     course = q.popleft()
        #     for neighbor in adj[course]:
        #         nodesprerequisites[neighbor].add(course)
        #         for prereq in nodesprerequisites[course]:
        #             nodesprerequisites[neighbor].add(prereq)
                
        #         indegree[neighbor] -= 1
        #         if indegree[neighbor] == 0:
        #             q.append(neighbor)

        # return [u in nodesprerequisites[v] for u, v in queries]

        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])
            indegrees[pre[1]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        nodespre = defaultdict(set)
        while queue:
            course = queue.popleft()
            for neighbor in adj[course]:
                nodespre[neighbor].add(course)
                for course_pre in nodespre[course]:
                    nodespre[neighbor].add(course_pre)
            
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        ans = []
        return [True if u in nodespre[v] else False for u, v in queries ]





