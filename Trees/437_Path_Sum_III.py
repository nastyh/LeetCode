# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:

        if not root:
            return 0
        
        def _helper(node, s):
            res = 0
            if not node:
                return res
            if node.val == s:
                res +=1
            return res + _helper(node.left, s - node.val) + _helper(node.right, s - node.val)
                
        
        return _helper(root, s) + _helper(root.left, s) + _helper(root.right, s)

        