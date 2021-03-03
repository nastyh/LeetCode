import collections
def countBattleships(board):
    m, n = len(board), len(board[0])
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    seen = set()
    dq = collections.deque([])
    cnt = 0
    # 1. find all potential battleships
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        if (x,y) not in seen:
            seen.add((x,y))
            cnt += 1
        for dx, dy in directions:
            if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][ y + dy]=='X' and (x + dx, y + dy) not in seen:
                seen.add((x + dx, y + dy))
    return cnt


def countBattleships_no_space(board):  # O(MN) and O(1)
    d = deque()
    res = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                d.append((row, col))
                board[row][col] = 'Y'
                res += 1
                while d:
                    r, c = d.popleft()
                    for row_offset, col_offset in [[r, c + 1], [r, c - 1], [r - 1, c], [r + 1, c]]:
                        if 0 <= row_offset < len(board) and 0 <= col_offset < len(board[0]) and board[row_offset][col_offset] == 'X':
                            d.append((row_offset, col_offset))
                            board[row_offset][col_offset] = 'Y'
                res += 1 
    return res 


def countBattleships_no_change(board):  # O(MN) and O(1)
    """
    If above cell and left cell is empty, increment ship count
    If they are not empty, we know they are part of a ship so leave the count as is
    """
    col_above = [0] * len(board[0])
    c = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                above_empty = False
                left_empty = False
                if col_above[j] == 0:
                    col_above[j] = 1
                    above_empty = True
                if j > 0:
                    if board[i][j - 1] != "X":
                        left_empty = True
                else:
                    left_empty = True
                    
                if above_empty and left_empty:
                    c += 1
            else:
                col_above[j] = 0        
    return c