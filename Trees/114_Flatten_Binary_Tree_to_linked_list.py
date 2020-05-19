# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root:
                return
            l = helper(root.left)
            r = helper(root.right)
            if l:
                root.right = l
                while l and l.right:
                    l = l.right
                l.right = r
                root.left = None
            return root

        return helper(root)

    def flatten_iter(root):
        from collections import deque
        from not root:
            return
        q = deque()
        dummy = TreeNode(0)
        it = dummy
        q.append(root)

        while q:
            t = q.popleft()
            if t.right:
                q.append(t.right)
            if t.left:
                q.append(t.left)

            it.right = t
            it = it.right
            it.left = it.right = None
        return dummy.right




if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(5)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.right = TreeNode(6)
    print(l.flatten(l))
