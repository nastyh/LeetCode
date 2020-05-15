# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self, root):
        #DFS
        if not root:
            return None
        if root and (not root.left and not root.right):
            return root
        if root.left and not root.right:
            return None
        if not root.left and root.right:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        #BFS
        # from collections import deque
        # if not root:
        #     return None
        # s = deque()
        # s.append(root)
        # while s:
        #     t = s.popleft()
        #     if t:
        #         t.left, t.right = t.right, t.left
        #         s.extend([t.right, t.left])

        # return root


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(7)
    l.left.left = TreeNode(1)
    l.left.right = TreeNode(6)
    l.right.left = TreeNode(3)
    l.right.right = TreeNode(1)
    # l.right.right = TreeNode(18)

print(l.invertTree(l))
