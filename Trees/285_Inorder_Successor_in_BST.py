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

    def inorderSuccessor_BST_property(self, root, p):  # O(H), O(H)
        res = None
        if not root: return
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p.val
        node = root
        while node.val != p.val:
            if p.val <= node.val:  # if the given value is smaller than the value kept in the helper node
                res = node  # we will need to go left. But we need to save a node from which we turned left
                node = node.left
            else:  # otherwise just turn right
                node = node.right
        return res.val if res else None

    
    def inorderSuccessor_stack(self, root, p):  # O(H), O(1)
        stack, prev, curr = [], None, None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            prev = curr
            curr = root
            if prev and prev.val == p.val:
                return curr
            root = root.right


if __name__ == '__main__':
    l = TreeNode(12)
    l.left = TreeNode(6)
    l.right = TreeNode(20)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(8)
    l.right.left = TreeNode(17)
    l.right.right = TreeNode(23)
    m = TreeNode(5)
    m.left = TreeNode(3)
    m.right = TreeNode(6)
    m.left.left = TreeNode(2)
    m.left.right = TreeNode(4)
    m.left.left.left = TreeNode(1)
    # print(l.inorderSuccessor(l, l.right.left))
    # print(l.inorderSuccessor_BST_property(l, l.right.left))
    print(m.inorderSuccessor_BST_property(m, m.right))

