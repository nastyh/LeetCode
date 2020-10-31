class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def kthSmallest(self, root, k):  # naive: O(n) and O(n + h)
        def _dfs(node):
            res, l, r = [], [], []
            if not root:
                return res
            res.append(node.val)
            if node.left:
                l = _dfs(node.left)
            if node.right:
                r = _dfs(node.right)
            return l + res + r
        out = _dfs(root)
        return out[k - 1]


    def kthSmallest_alt(self, root, k):  # just better time and space complexity: O(h + k) and O(k) in space b/c once we have k elements in res, we stop
        res, st = [], []
        if not root: return res
        while st or root:
            while root:
                st.append(root)
                root = root.left
            if st and not root:
                root = st.pop()
                res.append(root.val)
                root = root.right
                if len(res) == k:
                    return res[-1]

    
    def kthSmallest_another(self, root, k):  # O(h + k) time and O(h) space b/c we don't build res, but just keep a counter instead and for stack it's extra h
        res, st, counter = None, [], 0
        if not root: return res
        while st or root:
            while root:
                st.append(root)
                root = root.left
            if st and not root:
                root = st.pop()
                res = root.val
                counter += 1
                root = root.right
                if counter == k:
                    return res



if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(1)
    l.right = TreeNode(4)
    l.left.right = TreeNode(2)
    # print(l.kthSmallest(l, 1))
    # print(l.kthSmallest_alt(l, 1))
    m = TreeNode(5)
    m.left = TreeNode(3)
    m.right = TreeNode(6)
    m.left.left = TreeNode(2)
    m.left.right = TreeNode(4)
    m.left.left.left = TreeNode(1)
    # print(m.kthSmallest(l, 3))
    print(m.kthSmallest_alt(l, 3))
    print(m.kthSmallest_another(l, 3))
