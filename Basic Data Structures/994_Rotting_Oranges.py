from collections import deque
def orangesRotting(grid):  # O(MN and O(MN)
    """
    Traverse and put rotten cells into the queue. Make sure to mark them as visited 
    In parallel, checking two edge cases, when we don't have fresh or rotten at all
    Start the main portion
    We need an extra "for _ in range(neighbors_number)" loop, because we only increment res once we have seen all neighboring cells.
    It's because two neighoring cells get contaminated at the same time and we need to increment only once
    The caveat here is that we increment res one more extra time at the very end once everything has been processed.
    We account for this with return res - 1
    Prior to that need to check if there are any fresh cells left (for row in grid). It might be a case if they were surrounded by empty cells and there was no 
    way to contaminate them 
    """
    num_of_fresh, num_of_rotten = 0, 0
    d = deque()
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                num_of_fresh += 1
            if grid[row][col] == 2:
                d.append((row, col))
                visited[row][col] = True
                num_of_rotten += 1
    if num_of_fresh == 0:
        return 0
    if num_of_rotten == 0:
        return - 1
    while d:
        neighbors_number = len(d)
        for _ in range(neighbors_number):
            row, col = d.popleft()
            for row_offset, col_offset in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= row_offset < len(grid) and 0 <= col_offset < len(grid[0]) and visited[row_offset][col_offset] == False:
                    if grid[row_offset][col_offset] == 1:
                        visited[row_offset][col_offset] = True
                        grid[row_offset][col_offset] = 2
                        d.append((row_offset, col_offset))
        res += 1
        # if d:
        #     res += 1
    for row in grid:
        if any(i == 1 for i in row):
            return -1
    return res - 1


def orangesRotting_efficient(grid):  # O(MN) and O(1)
    """
    Same idea as above but instead of creating a matrix visited, mark visited cells in the original matrix with -1
    """
    num_of_fresh, num_of_rotten = 0, 0
    d = deque()
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                num_of_fresh += 1
            if grid[row][col] == 2:
                d.append((row, col))
                grid[row][col] = -1
                num_of_rotten += 1
    if num_of_fresh == 0:
        return 0
    if num_of_rotten == 0:
        return - 1
    while d:
        neighbors_number = len(d)
        for _ in range(neighbors_number):
            row, col = d.popleft()
            for row_offset, col_offset in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= row_offset < len(grid) and 0 <= col_offset < len(grid[0]) and grid[row_offset][col_offset] != -1:
                    if grid[row_offset][col_offset] == 1:
                        grid[row_offset][col_offset] = -1
                        grid[row_offset][col_offset] = 2
                        d.append((row_offset, col_offset))
        res += 1
    for row in grid:
        if any(i == 1 for i in row):
            return -1
    return res - 1



if __name__ == '__main__':
    print(orangesRotting([[2, 1, 1],[1, 1, 0],[0, 1, 1]]))
    print(orangesRotting([[2, 1, 1],[0, 1, 1],[1, 0, 1]]))
    print(orangesRotting([[0, 2]]))
    print(orangesRotting_efficient([[2, 1, 1],[1, 1, 0],[0, 1, 1]]))
    print(orangesRotting_efficient([[2, 1, 1],[0, 1, 1],[1, 0, 1]]))
    print(orangesRotting_efficient([[0, 2]]))