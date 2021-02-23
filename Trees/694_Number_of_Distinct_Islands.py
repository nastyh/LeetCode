from collections import deque
def numDistinctIslands_alt(grid):  # O(mn) both
    """
    BFS but keep track of the unique paths 
    """
    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    directions = [[1, 0],[0, 1],[-1, 0],[0, -1]]
    patterns = []
    path = []
    I = 0
    J = 0
    def explore(i, j):            
        visited[i][j] = True
        for dir_ in directions:
            i_=i + dir_[0]
            j_=j + dir_[1]
            if i_< len(grid) and i_>= 0 and j_< len(grid[0]) and j_>= 0 and not visited[i_][j_] and grid[i_][j_] == 1:
                path.add((i_ - I,j_ - J))
                explore(i_, j_)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == 1:
                path=set([(0,0)])
                I = i
                J = j
                explore(i, j)
                if path not in patterns:
                    patterns.append(path)
        return len(patterns)


def numDistinctIslands_BFS(grid):
    dirs = {(-1, 0, 'U'),(1, 0, 'D'),(0, -1, 'L'),(0, 1, 'R')}
    def bfs(row, col, grid):
        queue = deque([(row, col)])
        s = "S"
        while queue:
            row, col = queue.popleft()   
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                grid[row][col] = 0
                for dir in dirs:
                    # record shape 
                    s += dir[2]
                    neighbor = (row + dir[0], col + dir[1])
                    queue.append(neighbor)
            else:
            # record hitting water or out of bounds 
                s += 'X'
        return s
    pattern = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                shape = bfs(i, j, grid)
                                    # add shape to set 
                pattern.add(shape)
        # only unique shapes in set 
    return len(pattern)

if __name__ == '__main__':
    print(numDistinctIslands_alt([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
    print(numDistinctIslands_alt([[1, 0, 1],[1, 1, 1]]))
    print(numDistinctIslands_BFS([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
    print(numDistinctIslands_BFS([[1, 0, 1],[1, 1, 1]]))