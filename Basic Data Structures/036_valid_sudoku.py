class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        O(row*col) both --> but it's O(81) so it's kinda O(1)
        Concept:
        check that a given number isn't used in a row/col or in a 3 by 3 part of the grid

        Iterate
        If a current element is not a dot, we'll add the following tuples
        (row_ix, element)
        (element, col_ix)
        floor division by 3 b/c we need to check smaller cells, too

        Return true if everything is unique
        """
        res = []
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element != '.':
                    res += [(r, element), (element, c), (r // 3, c // 3, element)]
        return len(res) == len(set(res))

    def isValidSudoku_another(self, board: List[List[str]]) -> bool:
        """
        O(81)-->O(1) both 
        store sets of numbers that are present in each row, column, and sub-box of the board
        For each cell, it checks
        period is not good
        if it's in a set of the same row
        if it's in a set of the same col
        if it's in a set of the same 3x3 board
        If any, False, otherwise, add the current cell to the sets
        and keep going
        """
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == '.':
                    continue
                #check violations
                if (num in rows[row] or 
                    num in columns[col] or 
                    num in sub_boxes[(row // 3, col // 3)]):
                   return False
                rows[row].add(num)
                columns[col].add(num)
                sub_boxes[(row // 3, col // 3)].add(num)
        return True
