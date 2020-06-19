# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorderPredcessor(self, root, p): # create a list, return the previous value

        def _helper(root, li):
            if not root: return None
            if root.left: _helper(root.left, li)
            li.append(root.val)
            if root.right: _helper(root.right, li)
            return li

        values = _helper(root, [])
        p_ix = values.index(p.val)
        return values[p_ix - 1] if values[0] != values[p_ix] else None

    """
    if the node has the the left subtree, return the most right node of that subtree
    If the node doesn't have the left subtree, return the node from which you made the last right turn
    """

    def inorderPredcessor_BST_property(self, root, p):
        res = None
        if not root: return
        if p.left:
            t = p.left
            while t.right:
                t = t.right
            return t.val

        node = root
        while node.val != p.val:
            if node.val <= p.val:
                res = node
                node = node.right
            else:
                node = node.left
        return res.val if res else None




if __name__ == '__main__':
    l = TreeNode(12)
    l.left = TreeNode(6)
    l.right = TreeNode(20)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(8)
    l.right.left = TreeNode(17)
    l.right.right = TreeNode(23)
    print(l.inorderPredcessor(l, l.left))
    print(l.inorderPredcessor_BST_property(l, l.left))
