# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def countNodes(self, root):
        q, res = deque(), []
        if not root:
            return 0
        q.append(root)
        while q:
            t = q.popleft()
            res.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return res



if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.left = TreeNode(4)
    l.left.right = TreeNode(5)
    l.right.left = TreeNode(6)
    # l.right.right = TreeNode(14)
    print(l.countNodes(l))


