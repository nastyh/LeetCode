# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
        # if (root.left.val == p.val and root.right.val == q.val) or (root.left.val == q.val and root.right.val = p.val):
            return root

if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(5)
    l.right = TreeNode(1)
    l.left.left = TreeNode(6)
    l.left.right = TreeNode(2)
    l.left.right.left = TreeNode(7)
    l.left.right.right = TreeNode(4)
    l.right.left = TreeNode(0)
    l.right.right = TreeNode(8)

    print(l.lowestCommonAncestor(l, l.left, l.right)) # returns 3
