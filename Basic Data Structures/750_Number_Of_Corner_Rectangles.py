from collections import Counter
def countCornerRectangles(grid):  # O(RC^2) and O(C^2) where R and C are rows and cols
    """
    For each pair of 1s in the new row (say at new_row[i] and new_row[j]),create more rectangles where that pair forms the base.
    The number of new rectangles is the number of times some previous row had row[i] = row[j] = 1.
    """
    count = Counter()
    ans = 0
    for row in grid:
        for c1, v1 in enumerate(row):
            if v1:
                for c2 in range(c1 + 1, len(row)):
                    if row[c2]:
                        ans += count[c1, c2]
                        count[c1, c2] += 1
    return ans