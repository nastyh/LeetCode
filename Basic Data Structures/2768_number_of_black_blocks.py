from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        """
        O(k), where k is the black cells. For each black cell, we process at most 4 blocks
        O(min((m-1)*(n-1), 4k)) -- average, worst is O(mn) when almost everything is black

        each black cell may affect up to 4 different 2×2 blocks.
        For each black cell at position (i, j), the blocks that include it have top‐left corners at:
        i-1, j-1
        i-1, j
        i, j-1
        i, j
        plus, top left are within valid ranges

        Iterate over all black cells and for each, increment the count of black cells
        for every valid block that contains it (using a dictionary keyed by the block’s top-left coordinate).

        Determine the total number of blocks. This is given by (m-1)*(n-1)
        The number of blocks with 0 black cells equals the total blocks minus the number of blocks that have at least one black cell.
        For blocks recorded in the dictionary, increment the respective count (from 1 to 4) based on the number of black cells found.

        """
        total_blocks = (m - 1) * (n - 1)
        blockCount = {}
        
        # Process each black cell
        for i, j in coordinates:
            # A cell may contribute to up to 4 blocks.
            for x in [i - 1, i]:
                for y in [j - 1, j]:
                    if 0 <= x < m - 1 and 0 <= y < n - 1:
                        blockCount[(x, y)] = blockCount.get((x, y), 0) + 1
                        
        # Initialize the result array for counts [0, 1, 2, 3, 4]
        res = [0] * 5
        # Blocks with 0 black cells are those not touched by any black cell.
        res[0] = total_blocks - len(blockCount)
        
        # Update counts for blocks that have 1 to 4 black cells.
        for count in blockCount.values():
            res[count] += 1
        
        return res