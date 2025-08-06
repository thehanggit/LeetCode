class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # rows = len(mat)
        # cols = len(mat[0])
        # def valid(row, col):
        #     return 0 <= row < rows and 0 <= col < cols
        
        # queue = deque()
        # seen = set()
        
        # for row in range(rows):
        #     for col in range(cols):
        #         if mat[row][col] == 0:
        #             queue.append((row, col, 1))
        #             seen.add((row, col))
        
        # dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # while queue:
        #     row, col, length = queue.popleft()
        #     for dir in dirs:
        #         new_row, new_col = row + dir[0], col + dir[1]
        #         if (new_row, new_col) not in seen and valid(new_row, new_col):
        #             seen.add((new_row, new_col))
        #             queue.append((new_row, new_col, length + 1))
        #             mat[new_row][new_col] = length
        # return mat

        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j, 1))
                    seen.add((i, j))
        
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            row, col, length = queue.popleft()
            for dir in dirs:
                new_r = row + dir[0]
                new_c = col + dir[1]
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if (new_r, new_c) not in seen:
                        queue.append((new_r, new_c, length + 1))
                        seen.add((new_r, new_c))
                        mat[new_r][new_c] = length
        return mat