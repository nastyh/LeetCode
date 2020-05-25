# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        
        def _helper(node, path):
            if not node.left and not node.right:
                if sum(path) == s:
                    res.append(path)
                return res
            if node.left:
                _helper(node.left, path + [node.left.val])
            if node.right:
                _helper(node.right, path + [node.right.val])
        
        _helper(root, [root.val])
        return res
       
            
            