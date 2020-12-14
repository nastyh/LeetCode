 def exist(board, word):  # o(N * 3^L), N - num of cells, L, length of the word; O(L)
    def dfs(word, i, j, match_idx, directions, board, visited):
        if match_idx == len(word) - 1:
            return True
        # try all four directions
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            # if within the board, never visited, and matches the current char, keep matching the next char
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and visited[x][y] == False and board[x][y] == word[match_idx + 1]:
                visited[x][y] = True
                if dfs(word, x, y, match_idx + 1, directions, board, visited):
                    return True
                visited[x][y] = False
    m = len(board)
    n = len(board[0])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    visited = [[False for _ in range(n)] for _ in range(m)]
    # find the starting char
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                visited[i][j] = True
                match_idx = 0
                if dfs(word, i, j, match_idx, directions, board, visited):
                    return True
                visited[i][j] = False
    return False


def exist_dfs(board, word):
    if not board:
        return False
    h, w = len(board), len(board[0])
    def dfs_search(idx, x, y):
        
        if x < 0 or x == w or y < 0 or y == h or word[idx] != board[y][x]:
            # Reject if out of boundary, or current grid cannot match the character word[idx]
            return False
        if idx == len(word) - 1: 
            # Accept when we match all characters of word during DFS
            return True
        cur = board[y][x]
        # mark as '#' to avoid repeated traversal
        board[y][x] = '#'
        # visit next four neighbor grids
        found = dfs_search(idx + 1, x + 1, y) or dfs_search(idx + 1, x - 1, y) or dfs_search(idx + 1, x, y + 1) or dfs_search(idx + 1, x, y - 1)
        # recover original grid character after DFS is completed
        board[y][x] = cur
        return found
    return any(dfs_search(0, x, y) for y in range(h) for x in range(w))      