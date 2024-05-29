class Solution:
    def convert(self, s: str, numRows: int) -> str:  #O(mn) and O(n)
        # zigzag means the first col is full
        # the second col starts from the second from the top
        # generalizes till we get to the first (top) row
        if numRows == 1: return s
        res = ''
        for r in range(numRows):
            increment = 2 * (numRows - 1) # how much to move on the col level to the right
            for i in range(r, len(s), increment): # we will be stepping in increments
                res += s[i] # works for the first and the last rows
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s): # as long as we're in the middle row and inbounds (the last two statements)
                    res += s[i + increment - 2 * r]
        return res

    def convert_matrix(self, s: str, numRows: int) -> str:
        if num_rows == 1:
            return s

        n = len(s)
        sections = ceil(n / (2 * num_rows - 2.0))
        num_cols = sections * (num_rows - 1)

        matrix = [[" "] * num_cols for _ in range(num_rows)]

        curr_row, curr_col = 0, 0
        curr_string_index = 0

        # Iterate in zig-zag pattern on matrix and fill it with string characters.
        while curr_string_index < n:
            # Move down.
            while curr_row < num_rows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            curr_row -= 2
            curr_col += 1

            # Move up (with moving right also).
            while (
                curr_row > 0 and curr_col < num_cols and curr_string_index < n
            ):
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1

        answer = ""
        for row in matrix:
            answer += "".join(row)

        return answer.replace(" ", "")