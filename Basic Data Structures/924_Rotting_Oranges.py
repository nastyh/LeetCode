from collections import deque

def orangesRotting(grid):  # O(n) both
    queue = deque()
    # Step 1). build the initial set of rotten oranges
    fresh_oranges = 0
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1
    # Mark the round / level, _i.e_ the ticker of timestamp
    queue.append((-1, -1))
    # Step 2). start the rotting process via BFS
    minutes_elapsed = -1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        row, col = queue.popleft()
        if row == -1:
            # We finish one round of processing
            minutes_elapsed += 1
            if queue:  # to avoid the endless loop
                queue.append((-1, -1))
        else:
            # this is a rotten orange
            # then it would contaminate its neighbors
            for d in directions:
                neighbor_row, neighbor_col = row + d[0], col + d[1]
                if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                    if grid[neighbor_row][neighbor_col] == 1:
                        # this orange would be contaminated
                        grid[neighbor_row][neighbor_col] = 2
                        fresh_oranges -= 1
                        # this orange would then contaminate other oranges
                        queue.append((neighbor_row, neighbor_col))

    # return elapsed minutes if no fresh orange left
    return minutes_elapsed if fresh_oranges == 0 else -1


def orangesRotting_optimized(grid):  # O(N^2) and O(1)
    ROWS, COLS = len(grid), len(grid[0])
    # run the rotting process, by marking the rotten oranges with the timestamp
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def runRottingProcess(timestamp):
        # flag to indicate if the rotting process should be continued
        to_be_continued = False
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == timestamp:
                    # current contaminated cell
                    for d in directions:
                        n_row, n_col = row + d[0], col + d[1]
                        if ROWS > n_row >= 0 and COLS > n_col >= 0:
                            if grid[n_row][n_col] == 1:
                                # this fresh orange would be contaminated next
                                grid[n_row][n_col] = timestamp + 1
                                to_be_continued = True
        return to_be_continued
    timestamp = 2
    while runRottingProcess(timestamp):
        timestamp += 1
    # end of process, to check if there are still fresh oranges left
    for row in grid:
        for cell in row:
            if cell == 1:  # still got a fresh orange left
                return -1
    # return elapsed minutes if no fresh orange left
    return timestamp - 2