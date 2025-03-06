class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # graph = defaultdict(list)
        # for x, y in edges:
        #     graph[x].append(y)
        #     graph[y].append(x)
        
        # seen =  set(restricted)

        # def dfs(node):
        #     if node not in seen:
        #         seen.add(node)
        #         for neighbor in graph[node]:
        #             dfs(neighbor)
        
        # dfs(0)
        # return len(seen) - len(restricted)

        graphs = defaultdict(list)
        for a, b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

        seen = set()
        restricted = set(restricted)
        seen.add(0)

        def dfs(node):
            for neighbor in graphs[node]:
                if neighbor not in restricted and neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        dfs(0)
        
        return len(seen)



        
        