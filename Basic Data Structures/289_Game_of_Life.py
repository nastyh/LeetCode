from collections import deque
def gameOfLife(board):  # in-place
    directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]  
    for i in range(len(board)):
        for j in range(len(board[0])):
            live = 0                # live neighbors count
            for x, y in directions: # check and count neighbors in all directions
                if (i + x < len(board) and i + x >= 0) and (j + y < len(board[0]) and j + y >=0) and abs(board[i + x][j + y]) == 1:
                    live += 1
            if board[i][j] == 1 and (live < 2 or live > 3):     # Rule 1 or Rule 3
                board[i][j] = -1
            if board[i][j] == 0 and live == 3:                  # Rule 4
                board[i][j] = 2
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = 1 if(board[i][j] > 0) else 0
    return board


def gameOfLife_extra_space(board):
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
    rows = len(board)
    cols = len(board[0])
    copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            for neighbor in neighbors:
                r = (row + neighbor[0])
                c = (col + neighbor[1])
                if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                    live_neighbors += 1

            # Rule 1 or Rule 3        
            if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = 0
            # Rule 4
            if copy_board[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 1