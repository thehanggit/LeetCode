class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
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
        #                 if new_state not in visited:
        #                     visited.add(new_state)
        #                     queue.append((distance + 1, new_state))
        
        # return -1

########################## A* search algorithm ###############################
        rows = len(grid)
        cols = len(grid[0])
        target = (rows - 1, cols - 1)
        dirs = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        def manhattan_distance(row, col):
            return target[0] - row + target[1] - col
        
        state = (0, 0, k)
        queue = [(manhattan_distance(0, 0), 0, state)]
        seen = set([state])

        while queue:
            estimation, steps, (row, col, remain) = heapq.heappop(queue)

            # we can reach the target in the shortest path (manhattan distance)
            remain_min_distance = estimation - steps
            if remain_min_distance <= remain:
                return estimation

            for dx, dy in dirs:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_eliminations = remain - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)

                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        new_estimation = manhattan_distance(new_row, new_col) + steps + 1
                        heapq.heappush(queue, (new_estimation, steps + 1, new_state))
        return -1



