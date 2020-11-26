# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def findTilt(self, root):
        if not root: return 0
        if root and not root.left and not root.right: return 0
        res = 0
        def _helper(root):
            nonlocal res
            if not root: return 0
            left_tree = _helper(root.left)
            right_tree = _helper(root.right)
            tilt = abs(left_tree - right_tree)
            res += tilt
            return left_tree + right_tree + root.val
        _helper(root)
        return res


if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    m = TreeNode(4)
    m.left = TreeNode(2)
    m.right = TreeNode(9)
    m.left.left = TreeNode(3)
    m.left.right = TreeNode(5)
    m.right.right = TreeNode(7)