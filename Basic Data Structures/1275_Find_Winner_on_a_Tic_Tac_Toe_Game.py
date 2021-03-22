 def tictactoe(self, moves: List[List[int]]):  # O(rc) and O(1) b/c board of size 3 by 3 doesn't really count
    board = [[" " for i in range(3)]for j in range(3)]
    def wins(s):
        if board[0][0] == s and board[0][1] == s and board[0][2] == s: return True
        if board[1][0] == s and board[1][1] == s and board[1][2] == s: return True
        if board[2][0] == s and board[2][1] == s and board[2][2] == s: return True
        if board[0][0] == s and board[1][0] == s and board[2][0] == s: return True
        if board[0][1] == s and board[1][1] == s and board[2][1] == s: return True
        if board[0][2] == s and board[1][2] == s and board[2][2] == s: return True
        if board[0][0] == s and board[1][1] == s and board[2][2] == s: return True
        if board[0][2] == s and board[1][1] == s and board[2][0] == s: return True
        return False

    for k in range(len(moves)):
        i,j = moves[k]
        if k % 2:
            board[i][j] = 'O'
        else:
            board[i][j] = 'X'
    if wins('X'):
        return "A"
    elif wins('O'):
        return "B"
    elif len(moves) == 9:
        return "Draw"
    else:
        return "Pending"