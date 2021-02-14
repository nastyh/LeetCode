# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def subtreeWithAllDeepest_BFS(self, root):  # BFS  O(n) both 
        if not root: return

        def _helper(root):
            d = deque()
            res = []
            l = 0
            d.append((0, None, root))
            while d:
                l += 1
                for _ in range(len(d)):
                    curr = []
                    depth, parent, t = d.popleft()
                    res.append([depth, parent, t.val])
                    if t.left:
                        d.append((l, t.val, t.left))
                    if t.right:
                        d.append((l, t.val, t.right))
                # res.append(curr)
            return res

        values = _helper(root)
        values_sorted = sorted(values, reverse = True, key = lambda x: x[0])
        return values_sorted[0][1]

    def subtreeWithAllDeepest_DFS(self, root):

        def _helper(root, d):
            if not root: return root, d

            ln, ld = _helper(root.left, d + 1)
            rn, rd = _helper(root.right, d + 1)
            if ld > rd:
                return ln, ld + 1
            if rd > ld:
                return rn, rd + 1
            return root, ld + 1

        return _helper(root, 0)[0]


if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(5)
    l.right = TreeNode(1)
    l.left.left = TreeNode(6)
    l.left.right = TreeNode(2)
    l.right.left = TreeNode(0)
    l.right.right = TreeNode(8)
    l.left.right.left = TreeNode(7)
    l.left.right.right = TreeNode(4)
    print(l.subtreeWithAllDeepest_BFS(l))
    print(l.subtreeWithAllDeepest_DFS(l))
