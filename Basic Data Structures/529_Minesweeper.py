def updateBoard(board, click):
    def has_adj_mines(self, board, x, y):
    def is_mine(x, y):
        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return 0
        if board[x][y] == 'M':
            return 1
        return 0                
    num_adj_mines = is_mine(x + 1, y) + is_mine(x, y + 1) + is_mine(x - 1, y) + is_mine(x, y - 1) + is_mine(x - 1, y - 1) + is_mine(x + 1, y + 1) + is_mine(x + 1, y - 1) + is_mine(x - 1, y + 1)
    return num_adj_mines

    x, y = click[0], click[1]

    if not (0 <= x < len(board) and 0 <= y < len(board[0])):
        return

    if board[x][y] == 'M':
        board[x][y] = 'X'
        return board
    elif board[x][y] == 'E':
        num_adj_mines = self.has_adj_mines(board, x,y)
        
        if num_adj_mines:
            board[x][y] = str(num_adj_mines)
            
        else:
            board[x][y] = 'B'
            self.updateBoard(board, [x + 1, y])
            self.updateBoard(board, [x, y + 1])
            self.updateBoard(board, [x - 1, y])
            self.updateBoard(board, [x, y - 1])
            self.updateBoard(board, [x + 1, y + 1])
            self.updateBoard(board, [x + 1, y - 1])
            self.updateBoard(board, [x - 1, y + 1])
            self.updateBoard(board, [x - 1, y - 1])
        return board


def updateBoard_another(board, click):
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
         
    if not board: return board
    M = len(board)
    N = len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]
    # if click directly has mine, mark it as X and return
    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board
    # if board has 'E' then check neighbors
    if board[click[0]][click[1]] == "E":
        return dfs(click[0], click[1])