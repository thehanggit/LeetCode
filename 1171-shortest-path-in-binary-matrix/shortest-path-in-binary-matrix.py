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
        dirs = [[-1, 0], [1, 0], [-1, -1], [1, -1], [-1, 1], [1, 1], [0, 1], [0, -1]]
        q = deque()
        q.append([0, 0, 1])
        visited = set()
        visited.add((0, 0))

        if not grid or grid[0][0] or grid[rows-1][cols-1]:
            return -1

        while q:
            x, y, distance = q.popleft()
            if (x, y) == (rows-1, cols-1):
                return distance

            for dir in dirs:
                dx, dy = dir
                if 0 <= x  + dx <= rows - 1 and 0 <= y + dy <= cols - 1:
                    row = x + dx
                    col = y + dy
                    if grid[row][col] == 0 and (row, col) not in visited:
                        visited.add((row, col))
                        q.append((row, col, distance + 1))
        
        return -1 
            