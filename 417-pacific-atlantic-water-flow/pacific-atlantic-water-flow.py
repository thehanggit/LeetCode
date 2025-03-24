class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = deque()
        atlantic = deque()
        rows = len(heights)
        cols = len(heights[0])

        for row in range(rows):
            pacific.append((row, 0))
            atlantic.append((row, cols-1))
        for col in range(cols):
            pacific.append((0, col))
            atlantic.append((rows - 1, col))

        def bfs(queue):
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            reachable = set()
            while queue:
                x, y = queue.popleft()
                reachable.add((x ,y))
                for dx, dy in dirs:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols:
                        if (new_x, new_y) not in reachable and heights[x][y] <= heights[new_x][new_y]:
                            queue.append((new_x, new_y))
            return reachable

        pacific_reach = bfs(pacific)
        atlantic_reach = bfs(atlantic)
        # ans = []
        # for x, y in pacific_reach:
        #     if (x, y) in atlantic_reach:
        #         ans.append([x, y])
        
        # return ans
        return list(pacific_reach.intersection(atlantic_reach))
