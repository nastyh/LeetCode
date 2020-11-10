# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isValidBST(self, root): # iteratively, BFS
        if not root:
            return True
        s = []
        l, r = -math.inf, math.inf
        s.append([root, l, r])
        while s:
            node, l_min, r_max = s.pop()
            if not node:
                continue
            if node.val < l_min or node.val > r_max:
                return False
            if node.left:
                s.append([node.left, l_min, node.val])
            if node.right:
                s.append([node.right, node.val, r_max])
        return True

    def isValidVST_recursively(self, root):  # recursive approach
        def _helper(node, l, r):
            if not node:
                return True
            if node.val <= l or node.val >= r:
                return False
            if not _helper(node.left, l, node.val):
                return False
            if not _helper(node.right, node.val, r):
                return False
            return True
        return _helper(root, -math.inf, math.inf)


if __name__ == '__main__':
    l = TreeNode(5)
    l.left = TreeNode(1)
    l.right = TreeNode(7)
    l.right.left = TreeNode(6)
    l.right.right = TreeNode(9)
    # print(l.isValidBST(l))
    print(l.isValidVST_recursively(l))
    # print(l.isValidBST_inorder(l))




