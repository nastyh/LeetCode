from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        """
        O(dimensions)
        O(1) nothing to store 
        find where the rook is
        start from this location and look four side
        till you hit the boundaries:
        if you hit B, stop since it's a bishop
        if you hit p, increment and stop scanning in this direction
        keep going otherwise
        return res 
        """
        res = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'R':
                    rook_row, rook_col = r, c 
                    break 
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = rook_row, rook_col
            while 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == 'B':
                    break 
                if board[r][c] == 'p':
                    res += 1
                    break 
                r += dr
                c += dc 
        return res 
        