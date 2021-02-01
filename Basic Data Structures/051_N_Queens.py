def solveNQueens(n):  # O(n!) and O(n)
    def could_place(row, col, queens):
        for r, c in enumerate(queens):
            if c == col or row - r == abs(col - c): return False
        return True
    
    def place_queens(row, n, queens):
        if row == n: return [queens]
        result = []
        for col in range(n):
            if could_place(row, col, queens):
                result += place_queens(row + 1, n, queens + [col])
        return result
    
    result = place_queens(0, n, [])
    return [[''.join(['Q' if c == col else '.' for c in range(n)]) for col in queens] for queens in result]

    

    