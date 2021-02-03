"""
Chess Board Distances
In a chess game, the knight has a long way to go just to move two squares diagonally.

Visualization:
https://i.redd.it/0tjoe0vjdms11.png

Given a (row,column) location for a knight on a chess board, create a new 8x8 matrix where each square contains the minimum number of moves to get the knight from its initial location to that square.

Input:
initial_location = (7,6)
Output: The matrix depicted in the above pictorial.

Constraint: The knight has eight options for where to move:
offsets = [(-2, -1),(-1, -2),(-2, 1),(1, -2),(2, -1),(-1, 2),(2, 1),(1, 2)]
"""

from collections import deque
def chess_distances(x, y):  # O(n^2) both. Here n is 8
    """
    Initialize a board
    Keep in the deque both coordinates and the number of steps. Steps is what we need to put into cells.
    1 step means 2 cells in one direction and one in another. 
    Start a loop.
    Do usual checks in order not to fall out the bounds and not to get into a loop.
    If a cell contains a number != 0, it means that this cell has been visited. So we don't need an extra data structure for visited
    """ 
    board = [[0] * 8 for _ in range(8)]
    d = deque()
    d.append((x, y, 0))
    while d:
        step_x, step_y, step = d.popleft()
        board[step_x][step_y] = step
        for x_offset, y_offset in [(step_x - 2, step_y - 1), (step_x - 1, step_y - 2), (step_x - 2, step_y + 1), (step_x + 1, step_y - 2),\
            (step_x + 2, step_y - 1), (step_x - 1, step_y + 2), (step_x + 2, step_y + 1),(step_x + 1, step_y + 2)]:
            if 0 <= x_offset < 8 and 0 <= y_offset < 8 and board[x_offset][y_offset] == 0:
                d.append((x_offset, y_offset, step + 1))
    return board


if __name__ == '__main__':    
    print(chess_distances(7, 6))

 