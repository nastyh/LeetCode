# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def rangeSumBST(self, root, L, R):

        def _helper(node): # main solution
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




if __name__ == '__main__':
    l = TreeNode(10)
    l.left = TreeNode(5)
    l.right = TreeNode(15)
    l.left.left = TreeNode(3)
    l.right.left = TreeNode(7)
    l.right.right = TreeNode(18)

    print(l.rangeSumBST(l, 7, 15))