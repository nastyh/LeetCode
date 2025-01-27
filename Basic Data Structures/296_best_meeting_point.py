from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        O(nlogn + rows*cols) for sorting, where n is the num of houses
        rows*cols for traversing grid
        O(k) for storing rows and cols
        the optimal meeting point is at the median of the x-coordinates and the median of the y-coordinates of the houses. 
        This minimizes the Manhattan distance.  We sort the rows and cols lists to efficiently find the median point
        after finding the median row and col iterate thru rows and cols to calc the Manhattan distance to the med point
        and sum them up
        """
        rows = []
        cols = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # rows and cols with 1s
                    rows.append(r)
                    cols.append(c)

        rows.sort()  # Important for finding the median
        cols.sort()  # Important for finding the median

        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]

        total_distance = 0
        for r in rows:
            total_distance += abs(r - median_row)
        for c in cols:
            total_distance += abs(c - median_col)

        return total_distance