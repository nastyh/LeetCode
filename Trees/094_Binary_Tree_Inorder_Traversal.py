class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def inorderTraversal(self, root):
        st, res = [], []
        if not root: return res
        while st or root:
            while root:
                st.append(root)
                root = root.left
            if st and not root:
                root = st.pop()
                res.append(root.val)
                root = root.right
        return res


if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(2)
    l.right.left = TreeNode(3)
    print(l.inorderTraversal(l))