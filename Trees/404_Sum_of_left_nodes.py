# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
    def sumOfLeftLeaves(self, root):
        ls = 0
        if not root:
            return 0
        if root.left and (not root.left.left and not root.left.right):
            ls += root.left.val
            rs = self.sumOfLeftLeaves(root.right)
            return ls + rs
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



    def sumOfLeftLeaves_bfs(self, root):
        from collections import deque
        res = 0
        if not root:
            return 0
        q = deque()
        q.append(root)

        while q:
            t = q.popleft()
            if t.left and (not t.left.left and not t.left.right):
                res += t.left.val
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return res

if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)
    print(l.sumOfLeftLeaves(l))
    print(l.sumOfLeftLeaves_bfs(l))

