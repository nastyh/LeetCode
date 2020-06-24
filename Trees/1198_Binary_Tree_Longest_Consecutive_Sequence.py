from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def longestConsecutive(self, root):
        if not root: return 0
        res = 0
        d = deque()
        d.append((root, 1))
        while d:
            t, curr_l = d.popleft()
            res = max(res, curr_l)
            if t.left:
                if t.left.val - 1 == t.val:
                    curr_l += 1
                else: curr_l = 1
                d.append((t.left, curr_l))
            if t.right:
                if t.right.val - 1 == t.val:
                    curr_l += 1
                else: curr_l = 1
                d.append((t.right, curr_l))

        return res

if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(3)
    l.right.left = TreeNode(2)
    l.right.right = TreeNode(4)
    l.right.right.right = TreeNode(5)
    print(l.longestConsecutive(l))
    m = TreeNode(1)
    m.right = TreeNode(2)
    m.right.right = TreeNode(2)
    print(m.longestConsecutive(m))
