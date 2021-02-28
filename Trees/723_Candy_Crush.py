def candyCrush(board):  # O(mn) both: where m and n are rows and cols respectively
    """
    check 3 spots at a time to see if there is the same character and that character isn't 0
    Same thing, but vertically
    Go through the set of crushable locations, and edit the original board
    Shift candies down if there are zeroes below them
    work our way up, shifting the candies that were not crushed into their "fallen" position
    """
    m,n = len(board), len(board[0])
    stable = False
    while True:
        stable = True
        crushable = set()
        # 1. check for horizontal crushables 
        for x in range(m):
            for y in range(n - 2):
                if board[x][y] == board[x][y + 1] == board[x][y + 2] != 0:
                    stable = False
                    crushable.update([(x,y),(x,y + 1),(x,y + 2)])   
        # 2. check for vertical crushables
        for x in range(m - 2):
            for y in range(n):
                if board[x][y] == board[x + 1][y] == board[x + 2][y] != 0:
                    stable = False
                    crushable.update([(x, y),(x + 1, y),(x + 2, y)])
        # 5. if no candies were crushed, we're done
        if stable:
            return board
        # 3. crush the candies
        for x,y in crushable:
            board[x][y] = 0
        # 4. let the candies "fall"
        for y in range(n):
            offset = 0
            for x in range(m - 1, -1, -1): # loop through column backward
                k = x + offset
                if (x,y) in crushable: # this will help us put items at bottom of the board
                    offset += 1
                else:
                    board[k][y] = board[x][y] # notice the use of k
            # now that all items have been copied to their right spots, place zero's appropriately at the top of the board
            for x in range(offset): 
                board[x][y] = 0