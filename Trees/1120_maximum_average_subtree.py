import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximumAverageSubtree(root: Optional[TreeNode]) -> float:
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
        if not node: 
            return (0, 0)
        l_sum, l_count = _helper(node.left)
        r_sum, r_count = _helper(node.right)
        curr_sum = l_sum + r_sum + node.val
        curr_count = l_count + r_count + 1
        curr_ave = curr_sum / curr_count
        res = max(res, curr_ave)
        return (curr_sum, curr_count)

    _helper(root)
    return res

if __name__ == '__main__':
    # Example usage
    root = TreeNode(5, TreeNode(6), TreeNode(1))
    print(maximumAverageSubtree(root))  # Output should be the maximum average

    # Test case 1
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(maximumAverageSubtree(root1))  # Expected output: 3.0 (subtree with node 3)

    # Test case 2
    root2 = TreeNode(10, TreeNode(20, TreeNode(15), TreeNode(25)), TreeNode(30))
    print(maximumAverageSubtree(root2))  # Expected output: 25.0 (subtree with node 25)
