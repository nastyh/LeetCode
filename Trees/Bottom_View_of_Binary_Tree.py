class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def bottom_view(self, root):
        if not root: return
        res = []
        def _helper(root, li):
            if not root: return
            _helper(root.left, li)
            if not root.left and not root.right:
                li.append(root.val)
            _helper(root.right, li)
            return li
        return _helper(root, res)

l = TreeNode(7)
l.left = TreeNode(3)
l.right = TreeNode(11)
l.left.left = TreeNode(1)
l.right.left = TreeNode(2)
l.left.right = TreeNode(9)
l.right.right = TreeNode(14)

print(l.bottom_view(l))
