class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        en_r, en_c = entrance
        queue = deque([(en_r, en_c, 0)])
        seen = set([(en_r, en_c)])
        while queue:
            r, c, steps = queue.popleft()
            if (r, c) != (entrance[0], entrance[1]) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return steps
            for dir in dirs:
                new_r = r + dir[0]
                new_c = c + dir[1]
                if 0 <= new_r <= rows - 1 and 0 <= new_c <= cols-1 and (new_r, new_c) not in seen and maze[new_r][new_c] != "+":
                    seen.add((new_r, new_c))
                    queue.append((new_r, new_c, steps + 1))
                    
        return -1 


                

