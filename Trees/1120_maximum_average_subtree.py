import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        """
        O(n) both 
        DFS: 
        base case
        run on left and right 
        calculate the numerator and the denominator
        update res 
        """
        res = -math.inf
        def _helper(node):
            nonlocal res
            if not node: return (0, 0)
            l_sum, l_count = _helper(node.left)
            r_sum, r_count = _helper(node.right)
            curr_sum = l_sum + r_sum + node.val
            curr_count = l_count + r_count + 1
            curr_ave = curr_sum / curr_count
            res = max(res, curr_ave)
            return (curr_sum, curr_count)
        _helper(root)
        return res