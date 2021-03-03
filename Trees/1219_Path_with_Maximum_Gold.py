def getMaximumGold(grid):  # O(MN) * number of cells w/ gold. O(MN)
    m = len(grid)
    n = len(grid[0])
    visited = []
    for i in range(m):
        visited.append([False]*n)
    def dfs(i, j, temp):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] == True or grid[i][j] == 0:
            return 0
        ans1 = temp
        visited[i][j] = True
        if i + 1 < m:
            ans1 = max(ans1, dfs(i + 1, j, temp + grid[i + 1][j]))
        if i - 1 >= 0:
            ans1 = max(ans1, dfs(i - 1, j, temp + grid[i - 1][j]))
        if j + 1 < n:
            ans1 = max(ans1, dfs(i, j + 1,temp + grid[i][j + 1]))
        if j - 1 >= 0:
            ans1 = max(ans1, dfs(i,j - 1, temp + grid[i][j - 1]))
        visited[i][j] = False
        return ans1
        
    max_path = 0 
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                max_path = max(max_path, dfs(i, j, grid[i][j]))
    return max_path