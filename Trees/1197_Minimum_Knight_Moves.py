from collections import deque
def minKnightMoves(x, y):
    if x == 0 and y == 0: return 0
    d = deque()
    d.append((0, 0, 0))
    visited = set((0, 0))
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    while d:
        coord_x, coord_y, step = d.popleft()
        if coord_x == x and coord_y == y:
            return step
        for x_offset, y_offset in [(coord_x - 2, -1), (coord_x - 1, -2), (coord_x - 1, -2), (coord_x - 2, -1), (coord_x - 2, 1), (coord_x - 1, 2),\
            (coord_x - 1, 2), (coord_x - 2, 1)]:
            # if x_offset == x and y_offset == y:
            #     return step
            if ((x_offset, y_offset)) not in visited and x_offset != coord_x and y_offset != coord_y:
                d.append((x_offset, y_offset, step + 1))
                visited.add((x_offset, y_offset))
    return step


if __name__ == '__main__':
    print(minKnightMoves(4, -7))