from collections import deque

def shortestPath(grid, k):
    """
    O(mnk), grid dimensions and the num of obstacles 
    O(mnk) for the visited states and the queue

    """
    m, n = len(grid), len(grid[0])
    if k >= m + n - 2:
        return m + n - 2
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    d = deque([(0, 0, k, 0)]) # coordinates, elimination capacity, zero steps
    visited = set((0, 0, k)) # visited states: coordinates and the remaining eliminations
    while d:
        x, y, remaining_k, steps = d.popleft()
        if (x, y) == (m - 1, n - 1): # arrived to the end of the matrix
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy # new coordinates
            if 0 <= nx < m and 0 <= ny < n: # within the bounds
                new_k = remaining_k - grid[nx][ny] 
                if new_k >= 0 and (nx, ny, new_k) not in visited: # new good cell
                    visited.add((nx, ny, new_k)) 
                    d.append((nx, ny, new_k, steps + 1))
    return -1
