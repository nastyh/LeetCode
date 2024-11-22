# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        """
        O(n) both
        DFS output as the distance from the current node to node q and q, respectively.
        If the subtree does not contain p or q, the distance will be inf.
        The result is the minimum of dist_p + dist_q over all nodes in the tree.
        """
        result = [float('inf')]
        def dfs(node):
            if not node:
                return float('inf'), float('inf')

            left_p, left_q = dfs(node.left)
            right_p, right_q = dfs(node.right)
            curr_p = 0 if node.val == p else float('inf')
            curr_q = 0 if node.val == q else float('inf')
            dist_p = min(curr_p, left_p+1, right_p+1)
            dist_q = min(curr_q, left_q+1, right_q+1)
            result[0] = min(result[0], dist_p + dist_q)
            return dist_p, dist_q
        dfs(root)
        return result[0]