def upsideDownBinaryTree_recur(self, root):  # O(n) both
    """
    Recursive approach
    """
    if not root: return # edge case 
    def _helper(node):
        """Returns root of rotated tree."""
        if not node.left: return node
        ans = _helper(node.left)
        node.left.left = node.right
        node.left.right = node
        node.left = node.right = None 
        return ans 
    
    return _helper(root)