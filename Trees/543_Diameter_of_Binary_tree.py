# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def diameterOfBinaryTree(self, root):
        def _height(root):
        	if not root:
        		return 0
        	if root and not root.left and not root.right:
        		return 1
        	l = _height(root.left) + 1
        	r = _height(root.right) + 1 
        	m = max(l, r)
        	return m

        lh, rh = _height(root.left), _height(root.right)
        return max(lh, rh) + 1 


if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    # l.right = TreeNode(3)
    # l.left.left = TreeNode(4)
    # l.right.left = TreeNode(5)
    # l.right.right = TreeNode(18)

print(l.diameterOfBinaryTree(l))
