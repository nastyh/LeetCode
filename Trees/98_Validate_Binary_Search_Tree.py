# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool: # iteratively, BFS
        if not root:
            return True
        s = []
        l, r = -math.inf, math.inf
        s.append([root, l, r])
        while s:
            node, l_min, r_max = s.pop()
            if not node:
                continue
            if node.val < l_min or node.val > r_max:
                return False
            if node.left:
                s.append([node.left, l_min, node.val])
            if node.right:
                s.append([node.right, node.val, r_max])
            return True

    def isValidVST_recursively(self, root):  # recursive approach
        def _helper(node, l = -math.inf, r = math.inf):
            if not node:
                return True
            if node.val < l or node.val > r:
                return False

            if not self._helper(node.left, l, node.val):
                return False
            if not self._helper(node.right, node.val, r):
                return False
            return True

        return _helper(root)




