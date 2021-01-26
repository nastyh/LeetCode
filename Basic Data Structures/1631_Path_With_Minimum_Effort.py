import math
import heapq
from collections import deque
def minimumEffortPath_Dijkstra(heights):  # O(mn * log(mn)) and O(mn)
    """
    Time complexity: O(mn) to visit every cell. The heap will contain at most mn values and it will take log(mn) to resort it every time 
    a new value is arriving
    Space: it's O(2mn) b/c we have dp and visited
    Approach:
    It's a BFS approach combined with dp, thus, two extra lists of lists
    update the absolute difference between the current cell and adjacent cells in dp. At the same time, wlso push all the adjacent cells in a priority queue. 
    The priority queue holds all the reachable cells sorted by its value in dp, i.e the cell with minimum absolute difference
    with its adjacent cells would be at the top of the queue.
    Get the cell from the top of the queue curr and visit the current cell.
    For each of the 4 cells adjacent to the current cell, calculate the maxDifference which is the maximum absolute difference to reach
    the adjacent cell (r, c) from current cell (x, y)
If the current value of the adjacent cell (adjacentX, adjacentY) in the difference matrix is greater than the maxDifference, we must update that value with maxDifference
    """
    dp = [[math.inf] * len(heights[0]) for _ in range(len(heights))]
    visited = [[False] * len(heights[0]) for _ in range(len(heights))]
    dp[0][0] = 0
    d = []
    d.append((0, 0, 0))
    while d:
        diff, x, y = heapq.heappop(d)
        visited[x][y] = True
        for r, c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and not visited[r][c]:
                curr_diff = abs(heights[r][c] - heights[x][y])
                max_diff = max(curr_diff, dp[x][y])
                if dp[r][c] > max_diff:
                    dp[r][c] = max_diff
                    heapq.heappush(d,(max_diff, r, c) )
    return dp[-1][-1]


def minimumEffortPath_binary_search(heights):  # O(mn) both
    def _helper(mid):
        visited = [[False]* len(heights[0]) for _ in range(len(heights))]
        queue = [(0, 0)]  # x, y
        while queue:
            x, y = queue.pop(0)
            if x == len(heights) - 1 and y == len(heights[0]) - 1:
                return True
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < len(heights) and 0 <= adjacent_y < len(heights[0]) and not visited[adjacent_x][adjacent_y]:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-heights[x][y])
                    if current_difference <= mid:
                        visited[adjacent_x][adjacent_y] = True
                        queue.append((adjacent_x, adjacent_y))
    left = 0
    right = 10000000
    while left < right:
        mid = (left + right) // 2
        if _helper(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':  
    print(minimumEffortPath_Dijkstra([[1, 2, 2],[3, 8, 2],[5, 3, 5]]))
    print(minimumEffortPath_Dijkstra([[1, 2, 3],[3, 8, 4],[5, 3, 5]]))
    print(minimumEffortPath_Dijkstra([[1, 2, 1, 1, 1],[1, 2, 1, 2, 1],[1, 2, 1, 2, 1],[1, 2, 1, 2, 1],[1, 1, 1, 2, 1]]))
    print(minimumEffortPath_binary_search([[1, 2, 2],[3, 8, 2],[5, 3, 5]]))
    print(minimumEffortPath_binary_search([[1, 2, 3],[3, 8, 4],[5, 3, 5]]))
    print(minimumEffortPath_binary_search([[1, 2, 1, 1, 1],[1, 2, 1, 2, 1],[1, 2, 1, 2, 1],[1, 2, 1, 2, 1],[1, 1, 1, 2, 1]]))
    