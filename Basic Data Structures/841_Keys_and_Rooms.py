from collections import deque
def canVisitAllRooms_bfs(rooms):  # O(N + E) and O(N) where N is the number of rooms and E is the number of keys
    """
    Standard DFS
    Start with the first room. 
    They go and traverse every element (or key, to be exact) in this room.
    Keep building the visited set
    At the end of the day, this set should have exactly as many elements as there are rooms
    """
    visited = set()
    d = deque()
    d.append(0)
    visited.add(0)
    while d:
        keys = rooms[d.popleft()]  # a list with keys that are stored in the current room
        for key in keys:
            if key not in visited:
                visited.add(key)
                d.append(key)
    return len(visited) == len(rooms)



# def canVisitAllRooms(rooms):  # DON'T KNOW WHY IT'S NOT WORKING
#     for room_ix in range(len(rooms) - 1):
#         print(rooms[room_ix])
#         print(room_ix)
#         if any([i for i in rooms[room_ix]]) == room_ix + 1 or len(rooms[room_ix + 1]) == 0:
#             continue
#         else:
#             return False
#     return True


if __name__ == '__main__': 
    print(canVisitAllRooms_bfs([[1], [2], [3], []]))
    print(canVisitAllRooms_bfs([[1, 3],[3, 0, 1],[2],[0]]))
    print(canVisitAllRooms_bfs([[1, 3], [3, 0, 1, 2], [3], [0]]))
    # print(canVisitAllRooms([[1], [2], [3], []]))
    # print(canVisitAllRooms([[1, 3],[3, 0, 1],[2],[0]]))
    # print(canVisitAllRooms([[1, 3], [3, 0, 1, 2], [3], [0]]))