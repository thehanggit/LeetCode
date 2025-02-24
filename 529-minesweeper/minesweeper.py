class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        rows = len(board)
        cols = len(board[0])
        dirs = [[0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, 0], [1, -1], [1, 1]]
        queue = deque()
        queue.append(click)
        visited = set()
        visited.add(tuple(click))
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                count_mine = 0
                for dir in dirs:
                    if 0 <= x + dir[0] <= rows - 1 and 0 <= y + dir[1] <= cols - 1:
                        new_x = x + dir[0]
                        new_y = y + dir[1]
                        if board[new_x][new_y] == "M":
                            count_mine += 1
                
                if count_mine > 0:
                    board[x][y] = str(count_mine)
                else:
                    board[x][y] = "B"
                    for dir in dirs:
                        if 0 <= x + dir[0] <= rows - 1 and 0 <= y + dir[1] <= cols - 1:
                            new_x = x + dir[0]
                            new_y = y + dir[1]
                            if (new_x, new_y) not in visited:
                                queue.append((new_x, new_y))
                                visited.add((new_x, new_y))
        return board              
