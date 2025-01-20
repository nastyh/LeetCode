from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """
        O(m*n + k), mat sizes + len(arr)
        O(mn + m + n), dict + two lists 
        dict of the shape: value from the matrix: (its row, its col)
        two lists: num of how many cells are checked in each row/col respectively
        """
        m, n = len(mat), len(mat[0])
        d = {}
        row_count, col_count = [0] * len(mat), [0] * len(mat[0])
        # build the dict
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i, j)
        # go over the list arr 
        for ix, num in enumerate(arr):
            r, c = d[num] # extract the coordinates of the current number
            row_count[r] += 1 # update the respective row this num belongs to
            col_count[c] += 1 # update the respective col this num belongs to
            """
            if count of marked numbers in row_count[r] == num of columns --> row is marked
            it's because you have a row, let's say [4, 6, 2]. A number (i.e. a row) is painted 
            if all the cols for this row are painted. Means the number == num of cols. 
            In the example above, 4 means that for the first row all four cols have been painted
            And vice versa: 
            count of marked numbers in col_count[c] == num of rows --> col is marked
            """
            if row_count[r] == n or col_count[c] == m:
                return ix 
        return -1