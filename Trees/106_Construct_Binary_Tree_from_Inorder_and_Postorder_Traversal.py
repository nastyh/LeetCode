# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def buildTree(self, inorder, postorder):
        if inorder:
            root_val = postorder[-1]
            root = TreeNode(root_val)
        else:
            return None

        ix_of_root_in_inorder = inorder.index(root_val)
        root.left = buildTree(inorder[:ix_of_root_in_inorder], postorder[:ix_of_root_in_inorder])
        root.right = buildTree(inorder[ix_of_root_in_inorder+1:], postorder[ix_of_root_in_inorder:-1])

        return root
