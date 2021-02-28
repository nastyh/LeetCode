class TicTacToe:  # O(1) and O(n)
    """
    Define countersfor rows and columns of the 2 players per row, column and diagonal and anti-diagonal.
    """
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n 
        self.rows = [[0] * n for _ in range(2)]
        self.cols = [[0] * n for _ in range(2)]
        self.diag = [0] * 2
        self.anti = [0] * 2

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.rows[player - 1][row] += 1
        self.cols[player - 1][col] += 1
        if row == col: self.diag[player-1] += 1
        if row + col == self.n - 1: self.anti[player-1] += 1
        if self.n in (self.rows[player - 1][row], self.cols[player - 1][col], self.diag[player - 1], self.anti[player - 1]): return player
        return 0 


class TicTacToe_math:
    def __init__(self, n: int):
        self.b = [1] *(2 * n + 2)
        self.n = n

    def move(self, row, col, player):
        ind = player # 2 is player two
        if ind == 1: #3 is play one
            ind = 3
        self.b[row] *= ind
        self.b[col + self.n] *= ind
        if row == col:
            self.b[2 * self.n] *= ind
        if row + col == self.n - 1:
            self.b[2 * self.n + 1] *= ind
        if 3**self.n in self.b:
            return 1
        if 2**self.n in self.b:
            return 2
        return 0