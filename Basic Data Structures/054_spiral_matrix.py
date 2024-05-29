class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:  # O(mn)
        res = []
        start_row, end_row, start_col, end_col = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        # need four pointers: the angles of the matrix
        # will update them in order to keep covering the elements we haven't visited

        while start_row <= end_row and start_col <= end_col:
            # first row as it is or the topmost row we haven't yet visited
            for col in range(start_col, end_col + 1):
                res.append(matrix[start_row][col])
            # top right to bottom right (last col essentially). The rightmost col we haven't visited
            for row in range(start_row + 1, end_row + 1):
                res.append(matrix[row][end_col])
            # bottom right to bottom left (last row essentially). The bottommost row we haven't visited
            for col in range(end_col - 1, start_col - 1, -1):
                if start_row == end_row:
                    break
                res.append(matrix[end_row][col])
            # bottom left to top left. THe leftmost col we haven't visited
            for row in range(end_row - 1, start_row, -1):
                if start_col == end_col:
                    break
                res.append(matrix[row][start_col])
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1
        return res