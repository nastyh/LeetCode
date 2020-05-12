# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def findBottomLeftValue(self, root):
        from collections import deque
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        while q:
            curr_level = []
            for _ in range(len(q)):
                t = q.popleft()
                curr_level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(curr_level)
        return res[-1][0]



if __name__ == '__main__':
    l = TreeNode(2)
    l.left = TreeNode(1)
    l.right = TreeNode(3)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.right = TreeNode(6)
    print(l.findBottomLeftValue(l))
    print(l.isleft(l.val, l))
