# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def postorderTraversal(self, root):
        if not root:
            return []

        stack ,out= [], []
        node, prev = root, None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            # add check to see if right leaf was the last seen
            if not node.right or node.right == prev:
                prev = stack.pop()
                out.append(node.val)
                node = None
            # iterate to right subtree
            else:
                node = node.right
        return out

if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(6)
    l.left.left = TreeNode(1)
    # l.right.left = TreeNode(2)
    l.left.right = TreeNode(3)

print(l.postorderTraversal(l))

