class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        for course, pre in prerequisites:
            hashmap[course].append(pre)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if hashmap[course] == []:
                return True
            
            visited.add(course)
            for pre in hashmap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            hashmap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
            

