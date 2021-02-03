from collections import deque
def wallsAndGates(rooms):
    def _helper(i, j, dist, rooms):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[i]) or rooms[i][j] < dist:
            return
        rooms[i][j] = dist
        _helper(i + 1, j, dist + 1, rooms)
        _helper(i - 1, j, dist + 1, rooms)
        _helper(i, j - 1, dist + 1, rooms)
        _helper(i, j + 1, dist + 1, rooms)
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            if rooms[i][j] == 0:
                _helper(i, j, 0, rooms)


def wallsAndGates_bfs_optimal(rooms):  # O(mn) both. Space because in the worst case we'll instert everything to the deque
    """
    Throw all gates into the deque (b/c we need to start somewhere)
    Then unpack the deck and look around:
    if any of the cells around is empty, plant step into it and and add to the deque
    b/c we want to explore everything around this cell and also pass an increased step
    """
    d, step = deque(), 0
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                d.append((row, col, 0))
    while d:
        x, y, step = d.popleft()
        for x_offset, y_offset in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= x_offset < len(rooms) and 0 <= y_offset < len(rooms[0]) and\
            rooms[x_offset][y_offset] == 2147483647:
                rooms[x_offset][y_offset] = step + 1
                d.append((x_offset, y_offset, step + 1))


def wallsAndGates_alt(rooms):
    if not rooms: return
    m, n = len(rooms), len(rooms[0])
    def bfs(i, j):
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for x1,y1 in [(x + 1,y), (x - 1,y), (x,y - 1), (x,y + 1)]:
                if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and rooms[x1][y1] > rooms[x][y] + 1:
                    rooms[x1][y1] = rooms[x][y] + 1
                    queue.append((x1, y1))
    for i in range(m): 
        for j in range(n): 
            if rooms[i][j] == 0: bfs(i, j)


if __name__ == '__main__':
    print(wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))
    print(wallsAndGates_alt([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))
