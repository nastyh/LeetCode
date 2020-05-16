# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#naive solution: put all nodes into a list, find the min difference between two elements
    def minDiffInBST(self, root) :
        def _inorder(node):
            res = []
            if not node:
                return res
            res.append(node.val)
            return _inorder(node.left) + res + _inorder(node.right) # inorder traversal on a BST gives an ordered list!

        tr = _inorder(root)
        # here we are finding the min difference between any two elements in the list
        curr_m = math.inf
        for ix in range(len(tr) - 1):
            if tr[ix+1] - tr[ix] < curr_m:
                curr_m = tr[ix+1] - tr[ix]
        return curr_m


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(6)
    l.left.left = TreeNode(1)
    # l.right.left = TreeNode(2)
    l.left.right = TreeNode(3)

print(l.minDiffInBST(l))
