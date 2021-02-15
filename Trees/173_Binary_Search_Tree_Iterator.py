class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.pointer = -1
        self._helper(root)
        
    
    def _helper(self, root):  # helper to traverse the tree in order and save it in a list
        """
        Just normal recursive inorder traversal
        """
        if not root: return
        self._helper(root.left)
        self.nodes.append(root.val)
        self._helper(root.right)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.pointer < len(self.nodes) - 1:
            self.pointer += 1
            return self.nodes[self.pointer]
        """
        Don't actually need to do this check (but probably a good thing to do anyway). Can rather go with
        self.pointer += 1
        return self.nodes[self.pointer]
        """

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.pointer < len(self.nodes) - 1:
            return True
        else:
            return False
        """
        or just return self.pointer < len(self.nodes) - 1
        """


def inorder_generator(node):
    if node:
        yield from inorder_generator(node.left)
        yield node
        yield from inorder_generator(node.right)

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.iterator = iter(inorder_generator(root))
        self._next = None

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self._next:
            next_node = self._next
            self._next = None
            return next_node.val

        next_node = next(self.iterator, None)
        if next_node:
            return next_node.val
        else:
            return None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self._next:
            return True
        try:
            self._next = next(self.iterator)
        except StopIteration:
            return False
        return True


class BSTIterator:  # pseudo-recursion

    def __init__(self, root):
        # Stack for the recursion simulation
        self.stack = []
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)


    def _leftmost_inorder(self, root):
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left


    def next(self):
        """
        @return the next smallest number
        """
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val


    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0