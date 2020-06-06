# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def minDepth(self, root):
        if not root: return 0
        res = 1
        if root and not root.left and not root.right: return res

        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepthDFS(self, root):
        if not root: return 0
        l = self.minDepthDFS(root.left)
        r = self.minDepthDFS(root.right)

        if root.left and root.right:
            return min(l, r) + 1
        elif root.left:
            return l + 1
        elif root.right:
            return r + 1
        else:
            return 1




if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)

    print(l.minDepth(l))
