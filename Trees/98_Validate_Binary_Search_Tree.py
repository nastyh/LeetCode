# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # if not root:
        #     return True
        # if not root and (not root.left and not root.right): return True

        s, l_child = [], -math.inf
        while s or root:
            while root:
                s.append(root)
                root = root.left

            root = s.pop()
            if root.val <= l_child:
                return False
            l_child = root.val

            root = root.right

        return True
