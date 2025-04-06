class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # rows = len(grid)
        # cols = len(grid[0])
        # dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        # islands = 0

        # def dfs(row, col):
        #     if grid[row][col] == "1":
        #         grid[row][col] = "0"
        #         for dir in dirs:
        #             if 0 <= row + dir[0] <= rows - 1 and 0 <= col + dir[1] <= cols - 1:
        #                 new_row = row + dir[0]
        #                 new_col = col + dir[1]
        #                 dfs(new_row, new_col)
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == "1":
        #             dfs(i, j)
        #             islands += 1
        
        # return islands
        # rows = len(grid)
        # cols = len(grid[0])
        # dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        # nums_island = 0
        # def dfs(row, col):
        #     for dir in dirs:
        #         if 0 <= row + dir[0] <= rows - 1 and 0 <= col + dir[1] <= cols - 1:
        #             new_row = row + dir[0]
        #             new_col = col + dir[1]
        #             if grid[new_row][new_col] == "1":
        #                 grid[new_row][new_col] = "0"
        #                 dfs(new_row, new_col)
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == "1":
        #             nums_island += 1
        #             grid[i][j] = 0
        #             dfs(i, j)
                    
        # return nums_island

        # rows = len(grid)
        # cols = len(grid[0])
        # dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # num_of_islands = 0

        # def dfs(x, y):
        #     for dir in dirs:
        #         if 0 <= x + dir[0] <= rows - 1 and 0 <= y + dir[1] <= cols - 1:
        #             new_x = x + dir[0]
        #             new_y = y + dir[1]
        #             if grid[new_x][new_y] == "1":
        #                 grid[new_x][new_y] = "0"
        #                 dfs(new_x, new_y)
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == "1":
        #             num_of_islands += 1
        #             dfs(i, j)

        # return num_of_islands


####################################################################################################################
        # count = 0
        # rows = len(grid)
        # cols = len(grid[0])
        # parent = []
        # rank = []
        # dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == "1":
        #             parent.append(i*cols+ j)
        #             count += 1
        #         else:
        #             parent.append(0)
        #         rank.append(0)
        
        # def find(x):
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]

        # def union(x, y):
        #     nonlocal count
        #     rootx, rooty = find(x), find(y)
        #     if rootx != rooty:
        #         if rank[x] > rank[y]:
        #             parent[rooty] = rootx
        #         elif rank[x] < rank[y]:
        #             parent[rootx] = rooty
        #         else:
        #             parent[rooty] = rootx
        #             rank[rootx] += 1
        #         count -= 1

        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == "1":
        #             for dx, dy in dirs:
        #                 new_row = row + dx
        #                 new_col = col + dy
        #                 if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
        #                     union(row * cols + col, new_row * cols + new_col)
        # return count

        rows = len(grid)
        cols = len(grid[0])
        parent = []
        rank = []
        count = 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    parent.append(i*cols + j)
                    count += 1
                else:
                    parent.append(0)
                rank.append(0)
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                elif rank[rooty] > rank[rootx]:
                    parent[rootx] = rooty
                else:
                    parent[rootx] = rooty
                    rank[rooty] += 1
                count -= 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    for dx, dy in dirs:
                        if 0 <= row + dx < rows and 0 <= col + dy < cols and grid[row + dx][col + dy] == "1":
                            union(cols*row + col, cols*(row + dx) + (col + dy))
        
        return count

                


            

        