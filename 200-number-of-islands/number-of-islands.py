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

        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        num_of_islands = 0

        def dfs(x, y):
            for dir in dirs:
                if 0 <= x + dir[0] <= rows - 1 and 0 <= y + dir[1] <= cols - 1:
                    new_x = x + dir[0]
                    new_y = y + dir[1]
                    if grid[new_x][new_y] == "1":
                        grid[new_x][new_y] = "0"
                        dfs(new_x, new_y)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num_of_islands += 1
                    dfs(i, j)

        return num_of_islands
                        



            

        