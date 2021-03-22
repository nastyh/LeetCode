 def tictactoe(moves):  # O(rc) and O(1) b/c board of size 3 by 3 doesn't really count
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


def tictactoe_short(moves):  # O(rc) both probably
    """
    The logic is to increment(Player A) and decrement(Player B) the row, col and the 2 diagonal variables depending on who played and which row, col was played.
    After every move, we need to check if the value of the row, col, or the diagonal variables is 3 or -3. Whoever played in that turn is the winner.
    """
    n = 3
    rows, cols = [0] * n, [0] * n
    diag1 = diag2 = 0
    for index, move in enumerate(moves):
        i, j = move
        sign = 1 if index % 2 == 0 else -1
        rows[i] += sign
        cols[j] += sign
        if i == j:
            diag1 += sign
        if i + j == n-1:
            diag2 += sign
        if abs(rows[i]) == n or abs(cols[j]) == n or abs(diag1) == n or abs(diag2) == n:
            return 'A' if sign == 1 else 'B'
    return "Draw" if len(moves) == (n * n) else 'Pending'