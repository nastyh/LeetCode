"""
https://leetcode.com/discuss/post/2798371/blocksquare-phone-connect-four-modified-bsf77/
Create 2 d array of the connect four grid. Example 3x6 grid.
Display the grid after playing . play(column, color). Always start placing the color at the bottom row up

After play(0,'R'), looks like below

- - - - - - 
- - - - - - 
R - - - - - 


Additional parameter given called toWin: which is the number of consecutive same color in east, west, north, south direction, not diagonal.
Basically, find path from a certain location in grid using left,right, up & down movement of same color.
Example winner after play(2,'R') and toWin=5 as total Rs is 6 from position (0,2)

Y R R - - - 
Y Y R - - - 
R R R - - - 
"""

class ConnectFour:
    def __init__(self, rows=3, cols=6, toWin=4):
        """
        Initialize the Connect Four board.
        By default rows=3 and cols=6 (as in the examples).
        toWin: number of connected same-color pieces required to win.
        """
        self.rows = rows
        self.cols = cols
        self.toWin = toWin
        # Create the grid with '-' representing an empty cell.
        self.grid = [['-' for _ in range(self.cols)] for _ in range(self.rows)]
    
    def display(self):
        """Print the current board row by row."""
        for row in self.grid:
            print(" ".join(row))
        print()  # extra line for spacing
    
    def play(self, col, color):
        """
        Place a disc of the given color in the specified column.
        Discs are placed in the lowest available cell (i.e. bottom-up).
        Returns the row index where the disc was placed, or -1 if the column is full.
        """
        # Traverse from bottom row up
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == '-':
                self.grid[row][col] = color
                print(f"Played {color} in column {col} (row {row})")
                self.display()
                # Check win condition from the placed position
                if self.check_win(row, col):
                    print(f"Winner: {color} wins with a connected group of {self.toWin} or more!\n")
                return row
        print(f"Column {col} is full. Move cannot be played.")
        return -1

    def check_win(self, row, col):
        """
        Check if the disc placed at (row, col) forms a connected group
        of at least toWin discs (only in north, south, east, west, not diagonal).
        We do this by doing a DFS (flood fill) from the cell.
        """
        color = self.grid[row][col]
        visited = set()
        count = self._dfs(row, col, color, visited)
        # Debug print: count of connected same-colored cells.
        print(f"Connected count from ({row}, {col}) = {count}")
        return count >= self.toWin

    def _dfs(self, row, col, color, visited):
        """
        Depth-first search counting connected cells (up, down, left, right) that match color.
        """
        if (row, col) in visited:
            return 0
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return 0
        if self.grid[row][col] != color:
            return 0
        
        visited.add((row, col))
        count = 1  # current cell
        # Define movements: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            count += self._dfs(row + dr, col + dc, color, visited)
        return count


# Example demonstration:
# First example: After play(0, 'R')
print("Example 1: After play(0, 'R')")
game = ConnectFour(rows=3, cols=6, toWin=5)  # set toWin=5 as in the second example later if desired
game.play(0, 'R')

# For the second example we build up the board to reach:
# Y R R - - -
# Y Y R - - -
# R R R - - -
#
# This sequence of moves creates the winning group (6 R's connected from position (0,2)).
# The moves below simulate that sequence.
print("Example 2: Building a winning group with play(2, 'R')")
# Reset the board for demonstration
game = ConnectFour(rows=3, cols=6, toWin=5)

# Move sequence:
game.play(0, 'R')   # Column 0: bottom becomes R.
game.play(0, 'Y')   # Column 0: next available cell becomes Y.
game.play(0, 'Y')   # Column 0: top becomes Y.
game.play(1, 'R')   # Column 1: bottom becomes R.
game.play(1, 'Y')   # Column 1: next becomes Y.
game.play(1, 'R')   # Column 1: top becomes R.
game.play(2, 'R')   # Column 2: bottom becomes R.
game.play(2, 'R')   # Column 2: next becomes R.
# This move should trigger the win as it places R in the top of column 2.
game.play(2, 'R')   # Column 2: top becomes R (winning move).

# The final grid looks like:
# Y R R - - -
# Y Y R - - -
# R R R - - -
