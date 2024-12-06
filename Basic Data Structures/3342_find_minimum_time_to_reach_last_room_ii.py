class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        O((n*m)*log(n*m))
        O(2*n*m)
        BFS in general but 
        keep a marker for an odd/even day 
        next move is the max of being in the current cell's moveTime and waiting or current time plus 1 or 2
        """
        num_rows = len(moveTime)
        num_cols = len(moveTime[0])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        d = [(0, 0, 0, True)]  # time, row, col, is_day to account for odd/even days

        while d:
            time, row, col, is_day = heapq.heappop(d)
            # arrived at the last cell
            if row == num_rows - 1 and col == num_cols - 1:
                return time
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (new_row >= num_rows or new_col >= num_cols or 
                    new_row < 0 or new_col < 0 or visited[new_row][new_col]):
                    continue
                visited[new_row][new_col] = True
                additional_time = 1 if is_day else 2
                heapq.heappush(d, (max(time + additional_time, moveTime[new_row][new_col] + additional_time), new_row, new_col, not is_day))
        return -1

