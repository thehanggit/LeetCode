class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # max_row = len(grid) - 1
        # max_col = len(grid[0]) - 1
        # dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # state = (0, 0, k)
        # q = deque([(0, state)])
        # seen = set([state])

        # while q:
        #     distance, (row, col, k) = q.popleft()

        #     if (row, col) == (max_row, max_col):
        #         return distance
            
        #     for new_row, new_col in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
        #         if (0 <= new_row <= max_row) and (0 <= new_col <= max_col):
        #             new_eliminations = k - grid[new_row][new_col]
        #             new_state = (new_row, new_col, new_eliminations)

        #             if new_eliminations >= 0 and new_state not in seen:
        #                 seen.add(new_state)
        #                 q.append((distance + 1, new_state))

        # return -1

        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        state = (0, 0, k)
        queue = deque([(0, state)])
        seen = set([state])

        while queue:
            distance, (row, col, k) = queue.popleft()
            if (row, col) == (rows - 1, cols - 1):
                return distance
            
            for dir in dirs:
                if 0 <= row + dir[0] <= rows - 1 and 0 <= col + dir[1] <= cols - 1:
                    new_row = row + dir[0]
                    new_col = col + dir[1]
                    threshold = k - grid[new_row][new_col]
                    if threshold >= 0:

                        new_state = (new_row, new_col, threshold)
                        if new_state not in seen:
                            seen.add(new_state)
                            queue.append((distance + 1, new_state))
        
        return -1 


        # rows = len(grid)
        # cols = len(grid[0])
        # dirs = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        # queue = deque()
        # state = (0, 0, k)
        # queue.append((0, state))
        # visited = set([state])

        # while queue:
        #     distance, (row, col, k) = queue.popleft()
        #     if (row, col) == (rows-1, cols-1):
        #         return distance
            
        #     for dx, dy in dirs:
        #         new_row = row + dx
        #         new_col = col + dy
        #         if 0 <= new_row < rows and 0 <= new_col < cols:
        #             threshold = k - grid[new_row][new_col]
        #             if threshold >= 0:
        #                 new_state = (new_row, new_col, threshold)
        #                 if (new_row, new_col) not in visited:
        #                     visited.add(new_state)
        #                     queue.append((distance + 1, new_state))
        
        # return -1
