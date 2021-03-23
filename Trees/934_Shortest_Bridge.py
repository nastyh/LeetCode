from collections import deque
def shortestBridge(A):  # O(mn) both 
    """
    Paint the first encountered island with the color '2'
    Start expanding this island by painting connected 'empty' cells
    For every successive round, increase value of 'color' by 1 (This helps us keep track of the number of steps required)
    End when we bump into an island i.e. when we encounter a cell with value '1' (original island which wasn't colored '2')
    The answer is the difference of the current color value and '2' (the starting color)
    """
    def paint(A, i, j):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]) or A[i][j] == 0 or A[i][j] == 2:
            return
        A[i][j] = 2
        for nb in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            paint(A, i + nb[0], j + nb[1])
    # expanding from the perimeter of the island & incrementing color with every next outward move
    def expand(A, i, j, color):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]):
            return False
        if A[i][j] == 0:
            A[i][j] = color + 1
        return A[i][j] == 1
    if not A:
            return 0
        m, n, flag = len(A), len(A[0]), False
        # Finding and coloring the first encountered island
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if A[i][j] == 1:
                    paint(A, i, j)
                    flag = True
                    break
        # Growing outward and tracking number of steps taken to bump into other island
        for color in range(2, 2 + m + n + 1):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == color and ( expand(A, i - 1, j, color) or expand(A, i, j + 1, color) or expand(A, i + 1, j, color) or expand(A, i, j - 1, color)):
                        return color - 2


def shortestBridge(A):  # O(mn) both
    """
    Find the first island and turn all 1s into 2s
    Then start iterating over this island in a BFS manner
    If we find water (0) around, we will make it an island
    If we find another island (1) around, we will return step
    Step grows every time we looked up everything around the first island

    """
    row, col = len(A), len(A[0])
    dirs = [(0, 0), (-1, 0), (0, -1), (1, 0),(0, 1)]
    island1 = deque()
    def dfs(x, y):
        for dx, dy in dirs:
            if 0 <= x + dx < row and 0 <= y + dy < col and A[x + dx][y + dy] == 1:
                A[x + dx][y + dy] = 2
                island1.append([x + dx,y + dy])
                dfs(x + dx,y + dy)
    #DFS Find the first island and turn all 1 to 2
    def findIsland1():
        for x in range(row):
            for y in range(col):
                if A[x][y]:
                    return dfs(x, y)
    findIsland1()
    #BFS Expand the island and count step
    step = 0
    while island1:
        for _ in range(len(island1)):
            x, y = island1.popleft()
            for dx,dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and A[nx][ny] != 2:
                    if A[nx][ny] == 0:
                        A[nx][ny] = 2
                        island1.append([nx, ny])
                    elif A[nx][ny] == 1:
                        return step
        step += 1
    return step