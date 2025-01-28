# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        O(n), num of nodes
        O(h), height for the recursion stack
        helper function takes the current node, the direction we're moving,
        and the curr length of the path
        At every node, update the maximum length encountered so far.
        Recursive call:
        If the direction is "left", try moving to the left child (reset the length) and to the right child (increment the length).
        If the direction is "right", try moving to the right child (reset the length) and to the left child (increment the length).
        Start the traversal with both children 
        """
        if not root: return
        if root and not root.left and not root.right: return 0
        self.res = 0
        def _helper(node, direction, length):
            if not node: return
            self.res = max(self.res, length)
            if direction == 'l':
                _helper(node.left, 'l', 1)
                _helper(node.right, 'r', length + 1)
            else:
                _helper(node.right, 'r', 1)
                _helper(node.left, 'l', length + 1)

        _helper(root, 'l', 0)
        _helper(root, 'r', 0)
        return self.res