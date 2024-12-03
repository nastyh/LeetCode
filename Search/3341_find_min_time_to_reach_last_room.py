class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        O(rows * cols) both 
        get everything ready as usual
        start iterating using the deque
        temp_time is what we can do now plus 1 second 
        if this result is better than what we have as of now in res, update it 
        Build the res 
        """
        d = deque([[0, 0]])
        rows_ix, cols_ix = len(moveTime), len(moveTime[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = [[inf] * cols_ix for _ in range(rows_ix)]
        res[0][0] = 0
        while d:
            x, y = d.popleft()
            time = res[x][y]
            for dx, dy in directions:
                tx, ty = x+dx, y+dy
                if 0 <= tx < rows_ix and 0 <= ty < cols_ix:
                    temp_time = 1 + max(time, moveTime[tx][ty])
                    if temp_time < res[tx][ty]:
                        d.append([tx, ty])
                        res[tx][ty] = temp_time
        return res[-1][-1]