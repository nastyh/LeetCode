from collections import deque
def minKnightMoves(x, y):  # O(xy) both 
    """
    plain vanilla bfs
    start from zero, make steps to all sides 
    """
    if x == 0 and y == 0: return 0
    d = deque()
    d.append((0, 0, 0))
    visited = set((0, 0))
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    x, y = abs(x), abs(y)
    while d:
        coord_x, coord_y, step = d.popleft()
        if coord_x == x and coord_y == y:
            return step
        for dx, dy in directions:
            if ((coord_x + dx, coord_y + dy) not in visited) and ( step < 2 or (coord_x + dx >= 0 and coord_y + dy >= 0)): # d < 2, for x,y = (1,1) ans will be 4 without this ans is 2
                if coord_x + dx == x and coord_y + dy == y:
                    return step + 1
                d.append((coord_x + dx, coord_y + dy, step + 1))
                visited.add((coord_x + dx, coord_y + dy))  


def minKnightMoves_pruning(x, y):  # O(|x| * |y|) both
     q = deque([(0, 0, 0)])
    x, y, visited = abs(x), abs(y), set([(0, 0)])
    while q:
        a, b, step = q.popleft()
        if (a, b) == (x, y): return step
        for dx, dy in [(1, 2),(2, 1),(1, -2),(2, -1),(-1 ,2),(-2 ,1)]:  # no need to have (-1, -2) and (-2, -1) since it only goes 1 direction
            if (a + dx, b + dy) not in visited and -1 <= a + dx <= x + 2 and -1 <= b  +dy <= y  2:
                visited.add((a + dx, b + dy))
                q.append((a + dx, b + dy, step + 1))
    return -1 


def minKnightMoves_dfx(x, y):  # O(|x| * |y|) both
    """
    Try to move from target to origin as fast as possible
    When reaching to certain point, handle the special situation and return the result
    """
    @lru_cache(None) 
    def dp(x,y):
        if x + y == 0: return 0
        elif x + y == 2: return 2
        return min(dp(abs(x - 1),abs(y - 2)), dp(abs(x - 2),abs(y - 1))) + 1
    return dp(abs(x), abs(y))



def minKnightMoves_math(x, y):  # O(1)
    """
    find a pattern with division, which can replace the DFS process
    """
    x, y = abs(x), abs(y)
    if (x < y): x, y = y, x
    if (x == 1 and y == 0): return 3        
    if (x == 2 and y == 2): return 4        
    delta = x - y
    if (y > delta): return delta - 2 * int((delta - y) // 3);
    else: return delta - 2 * int((delta - y) // 4);


if __name__ == '__main__':
    print(minKnightMoves(4, -7))