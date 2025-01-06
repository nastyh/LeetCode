class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """
        O(mn) sizes of the maze
        O(mn) due to visited
        BFS
        helper to move and don't fall out the bounds
        """
        def _roll(maze, x, y, dx, dy):
            """
            starting position
            where to go as inputs
            """
            # check the boundaries
            while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
            return x, y

        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)] # not to get stuck 
        d = deque([start])
        visited[start[0]][start[1]] = True
        while d:
            x, y = d.popleft()
            if [x, y] == destination: # arrived 
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # look four sides 
                nx, ny = _roll(maze, x, y, dx, dy)
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    d.append((nx, ny))
        return False