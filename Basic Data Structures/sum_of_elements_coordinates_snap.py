"""
Image region with sum

Write code which determines whether the sum of all elements in a rectangular area 
in a square 2d array are equal to a target, and if true, prints out the coordinates 
(top left and bottom right) of a rectangular area which has the target sum.

Constraints:
- All elements in the array are positive
- The input array is valid (e.g all rows have the same length)
- If there are multiple solutions, any one is valid, don't need to find all

Example 1:
Input array:
[2, 6, 4]
[8, 3, 1]
[4, 5, 2]
Target:
20

Output:
[1,0], [2,1]
This region sums to 20:
[_, _, _]
[8, 3, _]
[4, 5, _]
"""

def find_target_rectangle_prefix_sum(matrix, target):
    """
    O(row^2 * cols^2)
    O(rows*cols) for the 2d prefix array
    numSubmatrixSumTarget counts all sub‑rectangles whose sum equals target and returns that count (an integer).
    The sliding‑window version stops as soon as it finds one rectangle that sums to target, and returns its coordinates (or None).
    Sliding‑window approach only works because you guaranteed all entries are positive (so you can safely shrink the window when you exceed target).
    """
    rows, cols = len(matrix), len(matrix[0])
    prefix_sum = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            top = prefix_sum[r - 1][c] if r > 0 else 0
            left = prefix_sum[r][c - 1] if c > 0 else 0
            top_left = prefix_sum[r - 1][c - 1] if min(r, c) > 0 else 0
            prefix_sum[r][c] = matrix[r][c] + top + left - top_left
    res = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    top = prefix_sum[r1 - 1][c2] if r1 > 0 else 0
                    left = prefix_sum[r2][c1 - 1] if c1 > 0 else 0 # removes elemts to the left of c1
                    top_left = prefix_sum[r1 - 1][c1 - 1] if min(r1, c1) > 0 else 0
                    cur_sum = prefix_sum[r2][c2] - top - left + top_left
                    if cur_sum == target:
                        # print(r1, c1, r2, c2)
                        res += 1
    return res   
       
def find_target_rectangle(matrix, target):
    """
    O(N^3) -- try all O(N^2) pairs of top/bottom rows, and for each do a sliding window (O(N))
    over columns
    O(N) to keep a single list of col sums 
    """
    n = len(matrix)
    # Iterate over all choices of top row
    for top in range(n):
        # col_sum[c] accumulates sums of column c from row=top..bottom
        col_sum = [0] * n
        # Extend bottom row downward
        for bottom in range(top, n):
            # Add row 'bottom' into our column‑sums
            for c in range(n):
                col_sum[c] += matrix[bottom][c]

            # Two‑pointer approach for positive entries
            curr = 0
            left = 0
            for right in range(n):
                curr += col_sum[right]
                # Shrink from the left while we're over target
                while curr > target and left <= right:
                    curr -= col_sum[left]
                    left += 1
                if curr == target:
                    # Return as two [row, col] lists
                    return [top, left], [bottom, right]

    # No matching rectangle
    return None