# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



    def largestValues(self, root):
        from collections import deque
        if not root:
            return None

        res = []
        q = deque()

        q.append(root)
        while q:
            values_in_level = []
            for _ in range(len(q)):
                t = q.popleft()
                values_in_level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(values_in_level)
        return [max(i) for i in res]

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(3)
    l.right = TreeNode(2)
    l.left.left = TreeNode(5)
    l.left.right = TreeNode(3)
    # l.right.left = TreeNode(5)
    l.right.right = TreeNode(9)

print(l.largestValues(l))

