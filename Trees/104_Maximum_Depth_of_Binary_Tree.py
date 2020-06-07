# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def maxDepth(self, root):
        def _helper(root):
            if not root: return 0
            if root and not root.left and not root.right: return 1
            if root.left:
                l = _helper(root.left)
            else: l = 0
            if root.right:
                r = _helper(root.right)
            else: r = 0
            return 1 + max(l, r)

        return _helper(root)

    def maxDepthBFS(self, root):
        if not root: return 0
        d, levels = deque(), 0
        d.append([root, 1])

        while d:
            t, curr_l = d.popleft()
            levels = max(levels, curr_l)
            if t.left:
                d.append([t.left, curr_l + 1])
            if t.right:
                d.append([t.right, curr_l + 1])
        return levels


if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.left.left = TreeNode(15)
    l.right.right = TreeNode(7)

    print(l.maxDepth(l))
    print(l.maxDepthBFS(l))
