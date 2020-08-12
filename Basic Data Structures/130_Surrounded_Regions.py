def solve(board):
    if len(board) == 0: return []
    for i in range(len(board[0])):
        if board[0][i] == 'O':
            board[0][i] = 'S'
        if board[-1][i] == 'O':
            board[-1][i] = 'S'
    for j in range(len(board)):
        if board[j][0] == 'O':
            board[j][0] = 'S'
        if board[j][-1] == 'O':
            board[j][-1] = 'S'
    def _helper(board, i, j):
        if board[i - 1][j] != 'S' and \
            board[i + 1][j] != 'S' and \
            board[i][j - 1] != 'S' and \
            board[i][j + 1] != 'S' and board[i][j] == 'O':
            board[i][j] = 'X'
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[0]) - 1):
            _helper(board, i, j)
    for i in range(len(board[0])):
        if board[0][i] == 'S':
            board[0][i] = 'O'
        if board[-1][i] == 'S':
            board[-1][i] = 'O'
    for j in range(len(board)):
        if board[j][0] == 'S':
            board[j][0] = 'O'
        if board[j][-1] == 'S':
            board[j][-1] = 'O'
    return board

def solve_recursion(board):
    def _helper(rid, cid):
        if rid < 0 or cid < 0 or rid > len(board) - 1 or cid > len(board[0]) - 1 or board[rid][cid] in ('X', 'E'):
            return
        board[rid][cid] = 'E'
        _helper(rid - 1, cid)
        _helper(rid + 1, cid)
        _helper(rid, cid - 1)
        _helper(rid, cid + 1)
    for rid, row in enumerate(board):
        for cid, column in enumerate(row):
            if rid == 0 or cid == 0 or rid == len(board) - 1 or cid == len(board[0]) - 1:
                if board[rid][cid] == 'O':
                    _helper(rid, cid)
    for rid, row in enumerate(board):
        for cid, column in enumerate(row):
            if board[rid][cid] == 'O':
                board[rid][cid] = 'X'
            if board[rid][cid] == 'E':
                board[rid][cid] = 'O'
    return board

if __name__ == '__main__':
    # print(solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]))
    print(solve([["O", "X", "X", "O", "X"],["X", "O", "O", "X", "O"],["X", "O", "X", "O", "X"],["O", "X", "O", "O", "O"],["X", "X", "O", "X", "O"]])) # doesn't pass on Leetcode: wrong test case?!
    print(solve_recursion([["O", "X", "X", "O", "X"],["X", "O", "O", "X", "O"],["X", "O", "X", "O", "X"],["O", "X", "O", "O", "O"],["X", "X", "O", "X", "O"]])) 

    """
    Output: [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","X","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    Expected: [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    """