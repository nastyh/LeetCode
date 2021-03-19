
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def tree2str(self, t):  # O(N) both 
        def _helper(node):
            if not node: return ''
            if node.left and node.right:
                l = '(' + _helper(node.left) + ')'
                r = '(' + _helper(node.right) + ')'
            elif node.left and not node.right:
                l = '(' + _helper(node.left) + ')'
                r = ''
            elif not node.left and node.right:
                l = '()'
                r = '(' + _helper(node.right) + ')'
            else:
                l = ''
                r = ''
            return str(node.val) + l + r
        return _helper(t)