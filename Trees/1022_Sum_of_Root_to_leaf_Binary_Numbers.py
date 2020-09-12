class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def sumRootToLeaf_2helpers(self, root):
        def _helper_traverse(root, curr, res):
            if not root:
                return res
            if root and not root.left and not root.right:
                res.append(curr)
            if root.left: _helper_traverse(root.left, curr + [root.left.val], res)
            if root.right: _helper_traverse(root.right, curr + [root.right.val], res)
            return res
        def _helper_binary(lists):
            res = 0
            for nums in lists:
                res += sum([2 ** k if v == 1 else 0 for k,v in enumerate(list(reversed(nums)))])
            return res
        numbers = _helper_traverse(root, [root.val], [])
        return _helper_binary(numbers)


if __name__ == '__main__':
    m = TreeNode(1)
    m.left = TreeNode(0)
    m.right = TreeNode(1)
    m.left.left = TreeNode(0)
    m.left.right = TreeNode(1)
    m.right.left = TreeNode(0)
    m.right.right = TreeNode(1)

    print(m.sumRootToLeaf_2helpers(m))


