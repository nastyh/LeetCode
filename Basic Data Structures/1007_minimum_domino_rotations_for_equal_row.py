import math
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        O(n), two passes of n
        O(1) nothing extra to store

        Greedy 
        we can pick any domino to try to reach. It has the upper and the lower value
        Three cases:
        make everything equal to the upper value
        make everything equal to the lower value
        Not possible to achieve 

        Emulate: pick the first domino
        try to get everyting == the upper
        not working, try to get everything == the lower
        work through the dominoes, track the best res 
        """
        def _helper(x):
            """
            returns the min value of rotations to make all upper = x
            or lower = x, or math.inf if not possible 
            pick the smallest outcome 
            """
            rotate_top, rotate_bottom = 0, 0 
            for top, bottom in zip(tops, bottoms): # processes both lists 
                if top != x and bottom != x:
                    return math.inf 
                if top != x:
                    rotate_top += 1
                if bottom != x:
                    rotate_bottom += 1
            return min(rotate_bottom, rotate_top)
        
        candidates = {tops[0], bottoms[0]}
        # we initialized candidates but we loop through the both lists
        res = min(_helper(candidate) for candidate in candidates)
        return -1 if res == math.inf else res 
        