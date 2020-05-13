# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def getAllElements(self, root1, root2):
        first, second = [], []

        def _helper(node):
            res = []
            if not node:
                return res
            res.append(node.val)
            return res + _helper(node.left) + _helper(node.right)

        first = _helper(root1)
        second = _helper(root2)

        return sorted(first + second)

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(5)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.right = TreeNode(6)

    r = TreeNode(32)
    r.left = TreeNode(2)
    r.right = TreeNode(10)
    r.left.left = TreeNode(3)
    r.left.right = TreeNode(4)
    r.right.right = TreeNode(10)


    print(l.getAllElements(l, r))
