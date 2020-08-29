# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def maxDepth(self, root):  # DFS
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


    def maxDepthBFS(self, root):  # BFS
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


    def maxDepth_helper(self, root):  # DFS but more elegant
        def _helper(root, res):
            if not root: return res
            l = _helper(root.left, res + 1)
            r = _helper(root.right, res + 1)
            return max(l, r)
        return _helper(root, 0)


if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.left.left = TreeNode(15)
    l.right.right = TreeNode(7)

    print(l.maxDepth(l))
    print(l.maxDepthBFS(l))
    print(l.maxDepth_helper(l))
