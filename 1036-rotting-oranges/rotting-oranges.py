class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        time, freshcount = 0, 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshcount += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        if freshcount == 0:
            return 0
        if not queue:
            return -1

        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        while queue and freshcount > 0:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dir in dirs:
                    new_x = i + dir[0]
                    new_y = j + dir[1]
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 2
                        freshcount -= 1
        if freshcount == 0:
            return time
        else:
            return -1
