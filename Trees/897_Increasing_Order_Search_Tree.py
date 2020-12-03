# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def increasingBST(self, root):  # O(n) and O(n)
        """
        Traverse in-order, you'll get them in the increasing order
        Start building a new tree using this list.
        Key here is to have the pointer res that points to the root of the tree, it's what we need to return
        Should we return t at the end, it will show the last element instead of the root 
        """
        elements = []
        def _helper(node):
            if not node:return
            _helper(node.left)
            elements.append(node.val)
            _helper(node.right)
        _helper(root)
        res = t = TreeNode(elements[0])
        for element in elements[1:]:
            t.right = TreeNode(element)
            t = t.right
        return res

    
    def increasingBST_alt(self, root):  # O(n) and O(h), where h is the tree's height
        """
        Without creating a list elements
        """
        def _helper(node):
            if node:
                _helper(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                _helper(node.right)
        res = self.curr = TreeNode(None)
        _helper(root)
        return res.right

    
    def increasingBST_recursion(self, root):
        def _helper(root, tail):
            if not root:
                return tail
            res = _helper(root.left, root)
            root.left = None
            root.right = _helper(root.right, tail)
            return res
        return _helper(root, None)

    

