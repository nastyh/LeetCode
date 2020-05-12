# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def kthSmallest(self, root, k):
        res = []
        if not root:
            return []
        res.append(root.val)
        l = self.kthSmallest(root.left, 0)

        r = self.kthSmallest(root.right, 0)
        return res + l + r

if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(1)
    l.right = TreeNode(4)
    l.left.right = TreeNode(2)
    print(l.kthSmallest(l, 0))
