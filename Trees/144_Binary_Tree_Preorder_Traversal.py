class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorderTraversal(self, root):
        res, st = [], []
        if not root: return res
        st.append(root)
        while st:
            t = st.pop()
            res.append(t.val)
            if t.right:
                st.append(t.right)
            if t.left:
                st.append(t.left)
        return res


if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(2)
    l.right.left = TreeNode(3)
    print(l.preorderTraversal(l))