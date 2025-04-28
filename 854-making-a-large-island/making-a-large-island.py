class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def explore_land(start):
            queue = [start]
            water =  set()
            area = 1
            dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

            while queue:
                i, j = queue.pop()
                for di, dj in dirs:
                    new_i = i + di
                    new_j = j + dj
                    if 0 <= new_i < m and 0 <= new_j < n:
                        if grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = -1
                            queue.append((new_i, new_j))
                            area += 1
                        elif grid[new_i][new_j] == 0:
                            water.add((new_i, new_j))
            
            for cell in water:
                water_area[cell] += area

        m, n = len(grid), len(grid[0])
        water_area = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    explore_land((i, j))
        if water_area:
            return 1 + max(water_area.values())

        return 1 if grid[0][0] == 0 else m*n
        