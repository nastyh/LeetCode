from collections import deque
def floodFill(image, sr, sc, newColor):  # O(G) where G is the number of pixels supposed to be painted. In the worst case O(RC)
    """
    Classical DFS
    Look in four directions: if not visited and is of the right color (start_color), then paint, update visited, add to the queue 
    """
    visited = [[False] * len(image[0]) for _ in range(len(image))]
    d = deque()
    d.append((sr, sc))
    start_color = image[sr][sc]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while d:
        x, y = d.popleft()
        visited[x][y] = True
        image[x][y] = newColor
        for x_offset, y_offset in directions:
            if 0 <= x + x_offset < len(image) and 0 <= y + y_offset < len(image[0]) and\
            visited[x + x_offset][y + y_offset] == False and image[x + x_offset][y + y_offset] == start_color:
                image[x + x_offset][y + y_offset] = newColor
                visited[x + x_offset][y + y_offset] = True
                d.append((x + x_offset, y + y_offset))
    return image 


def floodFill_DFS(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor: return image
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1: dfs(r - 1, c)
            if r + 1 < R: dfs(r + 1, c)
            if c >= 1: dfs(r, c - 1)
            if c + 1 < C: dfs(r, c + 1)
    dfs(sr, sc)
    return image