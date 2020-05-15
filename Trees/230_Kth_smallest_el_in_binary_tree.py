# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def kthSmallest(self, root, k):
        def _dfs(node):
            res, l, r = [], [], []
            if not root:
                return res
            res.append(node.val)
            if node.left:
                l = _dfs(node.left)
            if node.right:
                r = _dfs(node.right)
            return l + res + r # inorder traversal

        out = _dfs(root)
        # return sorted(out)[3]

        # return out
        # if len(out) <= k:
        return out[k-1] if k <= len(out) else None


     def kthSmallest_another(self, root, k):
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(1)
    l.right = TreeNode(4)
    l.left.right = TreeNode(2)
    print(l.kthSmallest(l, 0))

