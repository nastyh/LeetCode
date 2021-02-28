from collections import deque
def updateBoard_DFS(board, click):
    if not board: return board
    M = len(board)
    N = len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]
    
    def adjacent_mines(i, j):
        mines = 0
        for x, y in directions:
            if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "M":
                mines += 1
        return mines
    
    def dfs(i, j):
        # mark adjacent mine count at click position and return the board
        mines = adjacent_mines(i, j)
        if mines:
            board[i][j] = str(mines)
            return board
        # if no adjacent mines found then, do DFS
        board[i][j] = "B"
        for x, y in directions:
            if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "E":
                dfs(i + x, j + y)
        return board
        

    # if click directly has mine, mark it as X and return
    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board
    
    # if board has 'E' then check neighbors
    if board[click[0]][click[1]] == "E":
        return dfs(click[0], click[1])


def updateBoard_BFS(board, click):
    EMPTY = "E"
    MINE = "M"
    BLANK = "B"
    BOOM = "X"
    n = len(board)
    if n == 0: return board
    m = len(board[0])
    DIRECTIONS=[[1, 0],[-1, 0],[0, 1],[0, -1],[1, 1],[1, -1],[-1, 1],[-1, -1]]
    queue = deque()
    queue.append(click)
    while queue:
        row, col = queue.popleft()
        if board[row][col] == MINE:
            board[row][col] = BOOM
            return board
        elif board[row][col] == EMPTY:
            mines = []
            count = 0
            for d in DIRECTIONS:
                r = row + d[0]
                c = col + d[1]
                
                if r < 0 or c < 0 or r >= n or c >= m or (board[r][c] != EMPTY and board[r][c] != MINE):
                    continue
                elif board[r][c] == MINE:
                    count += 1
                mines.append([r,c])
            if count == 0:
                board[row][col] = BLANK
                queue.extend(mines)
            else:
                board[row][col] = str(count)
    return board