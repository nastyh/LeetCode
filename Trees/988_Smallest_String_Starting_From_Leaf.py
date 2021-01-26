import math
import string
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def smallestFromLeaf(self, root):
        P, s = '~', dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))
        def dfs(n, p):
            nonlocal P, s
            if not (n.left or n.right):
                if p < P: P = p
                return
            if n.left: dfs(n.left, s[n.left.val] + p)
            if n.right: dfs(n.right, s[n.right.val] + p)
        dfs(root, s[root.val])
        return P

if __name__ == '__main__': 
    l = TreeNode(0)
    l.left = TreeNode(1)
    l.right = TreeNode(2)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.left = TreeNode(3)
    l.right.right = TreeNode(4)
    print(l.smallestFromLeaf(l))