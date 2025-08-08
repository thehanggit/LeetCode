class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #using bfs
        # rows = cols = len(grid)
        # dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        # q = deque()
        # q.append([0, 0, 1])
        # visited = {(0, 0)}
        
        # if not grid or grid[0][0] or grid[rows-1][cols-1]:
        #     return -1

        # while q:
        #     row, col, distance = q.popleft()
        #     if (row, col) == (rows-1, cols-1):
        #         return distance
            
        #     for dir in dirs:
        #         x = row
        #         y = col
        #         if 0 <= x + dir[0] <= rows-1 and 0 <= y + dir[1] <= cols-1 and grid[x + dir[0]][y + dir[1]] == 0:
        #             x_new = x + dir[0]
        #             y_new = y + dir[1]
        #             if (x_new, y_new) not in visited:
        #                 visited.add((x_new, y_new))
        #                 q.append((x_new, y_new, distance + 1))
        # return -1


        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1, 0], [-1, -1], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
        queue = deque()
        seen = set()
        queue.append((0,0,1))
        seen.add((0,0))
        if not grid or grid[0][0] or grid[rows-1][cols-1]:
            return -1
        while queue:
            r, c, dist = queue.popleft()
            if (r, c) == (rows-1, cols-1):
                return dist

            for dir in dirs:
                new_r = dir[0] + r
                new_c = dir[1] + c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 0:
                    if (new_r, new_c) not in seen:
                        seen.add((new_r, new_c))
                        queue.append((new_r, new_c, dist+1))

        return -1
         
