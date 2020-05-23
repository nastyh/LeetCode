# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        root_val = preorder.pop(0)
        # root_ix = 0
        inorder_ix_of_root = inorder.index(root_val)

        l = self.buildTree(preorder, inorder[:inorder_ix_of_root])
        r = self.buildTree(preorder, inorder[inorder_ix_of_root + 1:])

        res = TreeNode(root_val)
        res.left = l
        res.right = r

        return res

