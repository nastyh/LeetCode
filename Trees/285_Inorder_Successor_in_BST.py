# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorderSuccessor(self, root, p): # create a list, return the next value

        def _helper(root, li):
            if not root: return None
            if root.left: _helper(root.left, li)
            li.append(root.val)
            if root.right: _helper(root.right, li)
            return li

        values = _helper(root, [])
        p_ix = values.index(p.val)
        return values[p_ix + 1] if values[-1] != values[p_ix] else None

    """
     if the node has the right subtree, return the most left node of that subtree
     if the node doesn't have the right subtree, return the node from which you made the last left turn
    """

    def inorderSuccessor_BST_property(self, root, p):
        res = None
        if not root: return
        if p.right:
            t = p.right
            while t.left:
                t = t.left
            return t.val

        node = root
        while node.val != p.val:
            if p.val <= node.val:
                res = node
                node = node.left
            else:
                node = node.right
        return res.val if res else None




if __name__ == '__main__':
    l = TreeNode(12)
    l.left = TreeNode(6)
    l.right = TreeNode(20)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(8)
    l.right.left = TreeNode(17)
    l.right.right = TreeNode(23)
    print(l.inorderSuccessor(l, l.right.left))
    print(l.inorderSuccessor_BST_property(l, l.right.left))
