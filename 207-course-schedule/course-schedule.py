class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodevisited = 0

        while queue:
            node = queue.popleft()
            nodevisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)

        return nodevisited == numCourses
        
            

