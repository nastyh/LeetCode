# class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # see the code: it's a BST, so if less, go left
        # if more, go right 
        if not root: return None # edge
        if root.val == val:
            return root  # match
        if val < root.val:  # go left
            return self.searchBST(root.left, val)
        if val > root.val:  # go right 
            return self.searchBST(root.right, val)