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
