# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        """
        O(n) to traverse the tree
        O(n) due to the recursion track
        deciding at each node whether it belongs to the “left tree” (all values ≤ target) or the “right tree” (all values > target).
        If the current node’s value is less than or equal to the target, then the entire left subtree of this node is guaranteed to be ≤ target
        then need to split its right subtree. After splitting, the left part of the split (from the right subtree) becomes
        the right child of the current node, and the right part becomes the overall right tree.
        if the current node’s value is greater than the target, then the entire right subtree is > target
        In this case, we split the left subtree and set the right part of that split as the current node’s left child.
        The left part of that split becomes the overall left tree.
        """
        if not root:
            return [None, None]
        # If the current node's value is less than or equal to target,
        # it belongs to the left subtree.
        if root.val <= target:
            # Recursively split the right subtree.
            leftSubtree, rightSubtree = self.splitBST(root.right, target)
            # Attach the left part of the split as the new right child.
            root.right = leftSubtree
            # The current node now becomes the root of the left tree.
            return [root, rightSubtree]
        else:
            # Otherwise, the node's value is greater than target and belongs to the right subtree.
            # Recursively split the left subtree.
            leftSubtree, rightSubtree = self.splitBST(root.left, target)
            # Attach the right part of the split as the new left child.
            root.left = rightSubtree
            # The current node becomes the root of the right tree.
            return [leftSubtree, root]