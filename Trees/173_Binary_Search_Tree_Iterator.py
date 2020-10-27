class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.pointer = -1
        self._helper(root)
        
    
    def _helper(self, root):  # helper to traverse the tree in order and save it in a list
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
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.pointer < len(self.nodes) - 1:
            return True
        else:
            return False


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
