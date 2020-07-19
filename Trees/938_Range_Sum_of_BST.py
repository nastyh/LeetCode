# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def rangeSumBST(self, root, L, R):

        def _helper(node): # main solution, takes O(n) extra space
            res = []
            if not node:
                return res
            res.append(node.val)
            return _helper(node.left) + res + _helper(node.right)

        return sum(i for i in _helper(root) if i >= L and i <= R)
# alternative

        def _helper_alt(node, L, R):
            res = []
            if not node:
                return res
            if node.val >= L and node.val <= R:
                res.append(node.val)
            return _helper(node.left) + res + _helper(node.right)

        # return sum(i for i in _helper(root) if i >= L and i <= R) # main solution
        return sum(_helper_alt(root, L, R)) # alternative solution

    def rangeSumBST_recurs(self, root, L, R):
        def _helper(node, L, R):
            res = 0
            if not node: return res
            if node:
                if L <= node.val <= R:
                    res += node.val
                if node.val > L:
                    res += _helper(node.left, L, R)
                if node.val < R:
                    res += _helper(node.right, L, R)
            return res
        return _helper(root, L, R)


    def rangeSumBST_recur_another(self, root, L, R):
        self.res = 0
        def _helper(root, L, R):
            if not root: return
            if root.val >= L and root.val <= R:
                self.res += root.val
            if root.val > L:
                _helper(root.left, L, R)
            if root.val < R:
                _helper(root.right, L, R)

        _helper(root, L, R)
        return self.res

if __name__ == '__main__':
    l = TreeNode(10)
    l.left = TreeNode(5)
    l.right = TreeNode(15)
    l.left.left = TreeNode(3)
    l.right.left = TreeNode(7)
    l.right.right = TreeNode(18)

    print(l.rangeSumBST(l, 7, 15))
    print(l.rangeSumBST_recurs(l, 7, 15))
    print(l.rangeSumBST_recur_another(l, 7, 15))
