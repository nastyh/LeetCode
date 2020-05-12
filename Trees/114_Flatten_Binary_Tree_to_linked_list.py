# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root:
                return
            l = helper(root.left)
            r = helper(root.right)
            if l:
                root.right = l
                while l and l.right:
                    l = l.right
                l.right = r
                root.left = None
            return root

        return helper(root)

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(5)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.right = TreeNode(6)
    print(l.flatten(l))
