class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """
        O(n)
        O(1)
        just do what it says
        helper functions aren't necessary
        for each element calculate the current diagonal
        if it's the largest diagonal we've seen, calculate res
        update the tracker of diagonals
        If we've seen such a diagonal, make a decision and pick a candidate
        with the bigger area
        """
        glob_diag = 0
        def _diag(x, y):
            return math.sqrt(x**2 + y**2)
        def _area(x, y):
            return x*y
        for dimension in dimensions:
            curr_diag = _diag(dimension[0], dimension[1])
            if curr_diag > glob_diag:
                res = _area(dimension[0], dimension[1])
                glob_diag = curr_diag
            elif curr_diag == glob_diag:
                res = max(res, _area(dimension[0], dimension[1]))
        return res
        
