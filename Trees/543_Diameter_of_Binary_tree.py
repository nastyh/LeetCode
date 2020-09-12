# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def diameterOfBinaryTree_alt(self, root):
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        if root is None:
            return 0  
        left_height = height(root.left)
        right_height = height(root.right)
        
        left_dia = self.diameterOfBinaryTree_alt(root.left)
        right_dia = self.diameterOfBinaryTree_alt(root.right)
        
        return max((left_height + right_height), max(left_dia, right_dia))
    
    

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.left = TreeNode(4)
    l.right.left = TreeNode(5)
    l.right.right = TreeNode(18)

print(l.diameterOfBinaryTree_alt(l))
