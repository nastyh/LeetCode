from collections import deque
import math
def maxLevelSum(self, root):  # O(n) both
    """
    Normal BFS but they key is to update res outside the for _ ... loop.
    Otherwise, we'll fail cases when the next level starts with a very big number (thus, making res = level) and then continues with a very small number. But we already moved 
    res.
    We need to get the total sum of the level before making any decision 
    """
    res = 1
    max_sum_seen = -math.inf
    if not root: return 0
    if root and not root.left and not root.right: return res
    d = deque()
    d.append((root, 1))   # node, curr_level
    while d: 
        level_sum = 0
        for _ in range(len(d)):
            t, level = d.popleft()
            level_sum += t.val
            if t.left:
                d.append((t.left, level + 1))
            if t.right:
                d.append((t.right, level + 1))
        if level_sum > max_sum_seen:  # this part is outside the for loop
                res = level
                max_sum_seen = level_sum 
    return res