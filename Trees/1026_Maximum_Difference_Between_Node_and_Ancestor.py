import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxAncestorDiff(self, root):

    def _helper(root,curr_min=math.inf, curr_max=-math.inf):
        
        curr_max = max(root.val,curr_max)
        curr_min = min(root.val,curr_min)
        
        result = abs(curr_max - curr_min)
        
        if root.left:
            result = max(result,_helper(root.left,curr_min,curr_max))
        
        if root.right:
             result = max(result,_helper(root.right,curr_min,curr_max))
        
        return result
    
    return _helper(root, math.inf, -math.inf)
    