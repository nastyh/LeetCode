# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def getMinimumDifference(self, root):
        self.min_diff = -math.inf
        values = []
        def inorder(node, values=values):
            if node:
                inorder(node.left)
                if values:
                    self.min_diff = min(self.min_diff, abs(node.val - values[-1]))

                values.append(node.val)
                inorder(node.right)

        inorder(root)
        return self.min_diff

if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(3)
    l.right.right = TreeNode(2)
    print(l.getMinimumDifference(l))
