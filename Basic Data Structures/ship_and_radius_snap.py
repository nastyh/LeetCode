"""
You have a ship centered at 0,0
Astroids located at {x,y} around the center contained in an array
The ship has a gun that can shoot at a distance r for radius and a spread shot that spreads at an angle of theta from the center of the ship.
Return the max amount of astroids that the ship can shoot with one shot.
"""

import math
from typing import List

def max_asteroids_in_spread(points: List[List[int]], r: float, theta: float) -> int:
    """
    O(nlog) for sorting and O(n) for the two-ponter run on the 2n-long list
    O(n) to store angles

    Compute d = sqrt(x^2 + y^2) and throw away the asteroids w/ d > r
    For each remaining asteroid, compute its polar angle
    alpha = atan2(y, x) * (180/pi) in [-180; 180]
    Sort the list of angles in an ascending order. 
    Then append each angle +;360° to the end of the list—this lets us handle wrap‑around across the 0°/360° boundary.
    Two pointers i <= j over this doubled list. For each i, advance j as far as angle[j] - angle[i] <= theha 
    Track the largest window size j - i + 1
    """
    # 1) Filter by radius
    angles = []
    for x, y in points:
        if x*x + y*y <= r*r:
            ang = math.degrees(math.atan2(y, x))
            angles.append(ang)
    if not angles:
        return 0
    # 2) Sort
    angles.sort()
    # 3) Duplicate with +360 to handle wrap
    m = len(angles)
    angles += [ang + 360.0 for ang in angles]

    # 4) Sliding window to find max number within 'theta'
    max_count = 0
    j = 0
    for i in range(m):
        # Expand j while within theta degrees
        while j < i + m and angles[j] - angles[i] <= theta:
            j += 1
        # [i, j) is the valid window
        max_count = max(max_count, j - i)

    return max_count

# Example
if __name__ == "__main__":
    asteroids = [[2,1], [2,2], [-1,1], [3,0], [0,-2]]
    r = 3.0
    theta = 90.0
    # Picks the 90° sector of radius 3 that covers the most points
    print(max_asteroids_in_spread(asteroids, r, theta))  # e.g. 3
