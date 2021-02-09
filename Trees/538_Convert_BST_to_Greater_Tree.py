class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def convertBST(self, root):  # O(n) and O(n)
        def _helper(node, val = 0):
            if node:
                node.val += _helper(node.right, val)
                return _helper(node.left, node.val)
            else:
                return val
        _helper(root)
        return root

    
    def convertBST_stack(self, root):  # O(n) both 
        total = 0
        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left
        return root

    
    def convertBST_Morris_Traversal(self, root):  # O(n) and O(1)
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ
                
        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root