import math
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def longestConsecutive_dfs(self, root):  # O(n) and O(n)
        if not root: return 0
        if root and not root.left and not root.right: return 1
        glob_res = -math.inf
        def _helper(node, parent, length):
            nonlocal glob_res
            if not node: return
            if parent and node.val == parent.val + 1:
                length += 1
            else:
                length = 1
            glob_res = max(glob_res, length)
            _helper(node.left, node, length)
            _helper(node.right, node, length)
        _helper(root, None, 0)
        return glob_res


    def longestConsecutive_iter(self, root):
        if not root: return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            node, l = stack.pop()
            res = max(l, res)
            if node.left:
                stack.append((node.left, l + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, l + 1 if node.right.val == node.val + 1 else 1))
        return res
    


if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(3)
    l.right.left = TreeNode(2)
    l.right.right = TreeNode(4)
    l.right.right.right = TreeNode(5)
    print(l.longestConsecutive_dfs(l))
    print(l.longestConsecutive_iter(l))
    m = TreeNode(1)
    m.right = TreeNode(2)
    m.right.right = TreeNode(2)
    print(m.longestConsecutive_dfs(m))
    print(m.longestConsecutive_iter(m))
