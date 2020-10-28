def treeToDoublyList(root):
    if not root:
        return None
    stack = [root]
    first, curr, last = None, root.left, None
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
            continue
        if stack:
            curr = stack.pop()
            if not first:
                first = curr
            if last:
                last.right = curr
                curr.left = last
            last = curr
            curr = curr.right
    first.left = last
    last.right = first
    return first


def treeToDoublyList_recur(root):
    self.prev = dummy = Node(-1) # intiate the global variant using dummy
        self.inOrder(root) # do the recursive inorder traversal
        if self.prev is not dummy: # if not root, the self.prev is dummy
            self.prev.right = dummy.right
            dummy.right.left = self.prev
        return dummy.right
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.prev.right = root # connect prev and curr
        root.left = self.prev
        self.prev = root #update self.prev
        self.inOrder(root.right)