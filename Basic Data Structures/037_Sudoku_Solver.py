def solveSudoku(board):  # O(9^(mn)) and O(mn)
    """
    Do not return anything, modify board in-place instead.
    """  
    def can_place(i, j, num):
        # Check row
        if any(num == n for n in board[i]):
            return False
        
        # Check col
        if any(num == n for n in list(zip(*board))[j]):
            return False
        
        # Check box
        start_row, start_col = (i // 3) * 3, (j // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if num == board[r][c]:
                    return False
        return True
    
    def find_unassigned():
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    return r, c
        return -1, -1
    
    def solve():
        r, c = find_unassigned()
        
        if r == -1 and c == -1:
            return True
        
        for num in [str(n) for n in range(1, 10)]:
            if can_place(r, c, num):
                board[r][c] = num
                if solve():
                    return True
                board[r][c] = '.'
        return False
    
    if not board:
        return
    solve()



def solveSudoku_another(board):
    n = len(board)
    rows, cols, boxes = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
    for r in range(n):
        for c in range(n):
            if board[r][c] == '.':
                continue
            v = int(board[r][c])
            rows[r].add(v)
            cols[c].add(v)
            boxes[(r // 3) * 3 + c // 3].add(v)

    def is_valid(r, c, v):
        box_id = (r // 3) * 3 + c // 3
        return v not in rows[r] and v not in cols[c] and v not in boxes[box_id]

    def backtrack(r, c):
        if r == n - 1 and c == n:
            return True
        elif c == n:
            c = 0
            r += 1

        # current grid has been filled
        if board[r][c] != '.':
            return backtrack(r, c + 1)

        box_id = (r // 3) * 3 + c // 3
        for v in range(1, n + 1):
            if not is_valid(r, c, v):
                continue

            board[r][c] = str(v)
            rows[r].add(v)
            cols[c].add(v)
            boxes[box_id].add(v)

            if backtrack(r, c + 1):
                return True

            # backtrack
            board[r][c] = '.'
            rows[r].remove(v)
            cols[c].remove(v)
            boxes[box_id].remove(v)

        return False

    backtrack(0, 0)