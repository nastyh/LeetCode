# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBalanced(self, root):
        def _helper(node):
            if not node: return 0
            return max(1 + _helper(node.left), 1 + _helper(node.right))

        if not root: return True
        else:
            l = _helper(root.left)
            r = _helper(root.right)
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(l - r) <= 1



if __name__ == '__main__':
    l = TreeNode(7)
    l.left = TreeNode(3)
    l.right = TreeNode(9)
    l.right.left = TreeNode(8)
    l.right.right = TreeNode(12)
    l.right.right.right = TreeNode(16)
    # print(l.isValidBST(l))
    # print(l.isValidBST_iter(l))
    print(l.isBalanced(l))

    m = TreeNode(1)
    m.left = TreeNode(2)
    m.right = TreeNode(2)
    m.left.left = TreeNode(3)
    m.left.right = TreeNode(3)
    m.left.left.left = TreeNode(4)
    m.left.left.right = TreeNode(4)
    print(m.isBalanced(m))
