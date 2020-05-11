# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
    def sumOfLeftLeaves(self, root):
        ls = 0
        if not root:
            return 0
        if root.left and (not root.left.left and not root.left.right):
            ls += root.left.val
            rs = self.sumOfLeftLeaves(root.right)
            return ls + rs
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)
    print(l.sumOfLeftLeaves(l))

