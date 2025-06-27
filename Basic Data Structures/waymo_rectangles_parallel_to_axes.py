"""
you are given an array of x-y points
return the min area of a rectangle formed from these points with
sides parallel to the x and y axes 
if possible
if no, -1
"""

from collections import defaultdict
import math


def min_area_rect(points):
    """
    O(n^2) b/c of two loops
    O(n) for the set to retrieve faster
    To form a rectangle aligned to the axes:
    need two points (x1, y1) and (x2, y2) so that 
    x1 != x2 and y1 != y2
    Then check if there are other two points 
    (x1, y2) and (x2, y1)
    also exist in the input 

    """
    point_set = set((x, y) for x, y in points)
    min_area = math.inf

    n = len(points)
    for i in range(n): # checking each possible pair: n(n-1) // 2
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Check for diagonal corners (must not be on same row or column)
            if x1 != x2 and y1 != y2:
                # Check if other two corners exist
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)

    return min_area if min_area != float('inf') else -1

def min_area_rect_optimized(points):
    """
    Sweep x from left to right.
    For each column (x-value), sort its y-values.
    For each y-pair in this column:
      If we've seen this y-pair in a previous column, we can form a rectangle.
      Area = horizontal distance between columns × vertical distance between y-pair.
      Keep track of the last x where each y-pair was seen.
    """
    x_to_ys = defaultdict(list)
    for x, y in points:
        x_to_ys[x].append(y)

    last_seen = {}  # (y1, y2) -> last x where we saw this y-pair
    min_area = math.inf

    for x in sorted(x_to_ys):
        ys = sorted(x_to_ys[x])
        # Check all pairs of y-values in this column
        for i in range(len(ys)):
            for j in range(i + 1, len(ys)):
                y1, y2 = ys[i], ys[j]
                if (y1, y2) in last_seen:
                    prev_x = last_seen[(y1, y2)]
                    area = (x - prev_x) * (y2 - y1)
                    min_area = min(min_area, area)
                # update last seen x for this y-pair
                last_seen[(y1, y2)] = x

    return min_area if min_area != math.inf else -1

