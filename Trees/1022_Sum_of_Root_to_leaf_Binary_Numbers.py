# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def sumRootToLeaf(self, root):
        res, l, r = [], [], []

        paths = []
        if not (root.left or root.right):
            return [[root.val]]
        if root.left:
            paths.extend([[root.val] + child for child in self.sumRootToLeaf(root.left)])
        if root.right:
            paths.extend([[root.val] + child for child in self.sumRootToLeaf(root.right)])
        return paths

        # return res + [i for i in (self.sumRootToLeaf(root.left) + self.sumRootToLeaf(root.right))]


        # return res

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(0)
    l.right = TreeNode(1)
    l.left.left = TreeNode(0)
    l.right.left = TreeNode(1)
    l.right.left = TreeNode(0)
    l.right.right = TreeNode(1)

print(l.sumRootToLeaf(l))

