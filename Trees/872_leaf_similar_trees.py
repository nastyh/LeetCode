# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    O(N1 + N2) both, where N1 and N2 are the trees' lengths
    Usual DFS. If no children, means it's the last level, add to curr_res
    Recursively run on the children, dragging curr_res with you
    """
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return False
        if root1 and not root2: return False
        if not root1 and root2: return False 
        def _helper(node, curr_res):
            if not node: return
            if not node.left and not node.right:
                curr_res.append(node.val)
            _helper(node.left, curr_res)
            _helper(node.right, curr_res)
            return curr_res
        r1, r2 = _helper(root1,[]), _helper(root2, [])
        print(f"value of r1 is {r1}")
        print(f"value of r2 is {r2}")
        return r1 == r2