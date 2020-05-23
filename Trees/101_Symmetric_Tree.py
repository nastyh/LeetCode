# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def isSymmetric(self, root):
        if not root:
            return True
        # if root and (not root.left and not root.right):
        #     return True

        def _helper(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False


            return _helper(l.left, r.right) and _helper(l.right, r.left)

        return _helper(root.left, root.right)


    def isSymmetric_iter(self, root):
        if not root:
            return True
        q = deque()
        q.append([root.left, root.right])
        while q:
            all_nodes = q.pop()
            l = all_nodes[0]
            r = all_nodes[1]

            if not l and not r:
                continue
            if l is None or r is None:
                return False
            if l.val == r.val:
                q.append([l.left, r.right])
                q.append([l.right, r.left])
            else:
                return False
        return True




if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(2)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.left = TreeNode(4)
    l.right.right = TreeNode(3)

# print(l.isSymmetric(l))
print(l.isSymmetric_iter(l))

