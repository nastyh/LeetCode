# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insertIntoBST(self, root, val):  # Recursive
        if not root:
            root = TreeNode(val)
        if val > root.val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        elif val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        else: root = TreeNode(val)
        return root
        

    def insertIntoBST_iter(self, root, val):  # iteratively
        if not root:
            root = TreeNode(val)
            return root
        t = root
        while t:
            if val < t.val:
                if not t.left:
                    t.left = TreeNode(val)
                    return root
                else:
                    t = t.left
            else:
                if not t.right:
                    t.right = TreeNode(val)
                    return root
                else:
                    t = t.right
