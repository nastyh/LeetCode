# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorderSuccessor(self, root, p):

        def _helper(root, li):
            if not root: return None
            if root.left: _helper(root.left, li)
            li.append(root.val)
            if root.right: _helper(root.right, li)
            return li

        values = _helper(root, [])
        p_ix = values.index(p.val)
        return TreeNode(values[p_ix + 1]) if values[-1] != values[p_ix] else None

