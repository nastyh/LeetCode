# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:  # O(N) both
        if not root:
            return None
        if root.val == L:
            root.left = None
            root.right = self.trimBST(root.right, L, R)
            return root
        if root.val == R:
            root.right = None
            root.left = self.trimBST(root.left, L, R)
        if root.val > R and root.val > L:
            return self.trimBST(root.left, L, R)
        if root.val < L and root.val < L:
            return self.trimBST(root.right, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

       # iterative
       def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:  # O(N) both
        if root is None: return None

        while root and (root.val < L or root.val > R):
            if root.val < L: root = root.right
            else: root = root.left

        lnode = rnode = root
        while lnode.left:
            if lnode.left.val < L:
                lnode.left = lnode.left.right
            else: lnode = lnode.left
        while rnode.right:
            if rnode.right.val > R:
                rnode.right = rnode.right.left
            else: rnode = rnode.right
        return root
