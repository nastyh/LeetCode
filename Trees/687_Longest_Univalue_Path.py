# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    def longestUnivaluePath(self, root):  # O(N) and O(h)
        """
        For each node, we want to know what is the longest possible arrow extending left,
        and the longest possible arrow extending right
        """
        ans = 0
        def _helper(node):
            if not node: return 0
            left_length = _helper(node.left)
            right_length = _helper(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            ans = max(ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        _helper(root)
        return ans