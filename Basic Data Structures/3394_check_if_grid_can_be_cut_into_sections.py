import bisect
from typing import List


class Solution:
    def checkValidCuts_sort(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        O(rlogr), r -- num of rectangles
        O(1), in-place sorting
        sorts the rectangles along the chosen dimension
        iterates through the sorted list to detect gaps (non-overlapping regions) that represent potential cut lines.
        At least 2 gaps are needed to partition the grid into 3 sections.
        checks both vertical and horizontal cuts and returns True if either approach yields valid cuts.
        """
        # Check if valid cuts can be made in a specific dimension
        def _check_cuts(rectangles: list[list[int]], dim: int) -> bool:
            """
            checks if there exist at least 2 non-overlapping gaps
            (or "cut points") along a specified dimension (either horizontal or vertical).
            These gaps represent positions where a cut can be made without slicing any rectangle.
            dim = 0 --> checks for valid vertical cuts
            dim = 1 --> checks for valid horizontal cuts
            """
            gap_count = 0

            # Sort rectangles by their starting coordinate in the given dimension
            rectangles.sort(key=lambda rect: rect[dim])

            # Track the furthest ending coordinate seen so far
            furthest_end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]

                # If current rectangle starts after the furthest end we've seen,
                # we found a gap where a cut can be made
                if furthest_end <= rect[dim]:
                    gap_count += 1

                # Update the furthest ending coordinate
                furthest_end = max(furthest_end, rect[dim + 2])

            # We need at least 2 gaps to create 3 sections
            return gap_count >= 2

        # Try both horizontal and vertical cuts
        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        times out for n = 60000
        """
        def check_cuts(cuts, axis):
            cut_positions = sorted(cuts)
            for i in range(len(cut_positions)):
                for j in range(i+1, len(cut_positions)):
                    cut1, cut2 = cut_positions[i], cut_positions[j]
                    group_bottom = group_mid = group_top = False
                    valid = True
                    for rect in rectangles:
                        low, high = rect[axis], rect[axis + 2]  # For x-axis, this is startx and endx; for y-axis, starty and endy.
                        # Check if rectangle is completely on the "bottom" (or left) side.
                        if high <= cut1:
                            group_bottom = True
                        # Check if rectangle is completely in the middle.
                        elif low >= cut1 and high <= cut2:
                            group_mid = True
                        # Check if rectangle is completely on the "top" (or right) side.
                        elif low >= cut2:
                            group_top = True
                        else:
                            # This rectangle straddles a cut.
                            valid = False
                            break
                    if valid and group_bottom and group_mid and group_top:
                        return True
            return False

        y_candidates = set()
        for rect in rectangles:
            y_candidates.add(rect[1])  # starty
            y_candidates.add(rect[3])  # endy
        # Similarly, candidate x boundaries for vertical cuts.
        x_candidates = set()
        for rect in rectangles:
            x_candidates.add(rect[0])  # startx
            x_candidates.add(rect[2])  # endx

        # Check horizontal cuts (axis = 1).
        if check_cuts(y_candidates, axis=1):
            return True

        # Check vertical cuts (axis = 0).
        if check_cuts(x_candidates, axis=0):
            return True

        return False