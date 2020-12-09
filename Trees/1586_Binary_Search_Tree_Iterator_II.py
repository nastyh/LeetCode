class BSTIterator:

    def __init__(self, root: TreeNode):  # O(N) and O(N)
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        self.arr = inorder(root)
        self.n = len(self.arr)
        self.pointer = -1

    def hasNext(self):  # O(1)
        return self.pointer < self.n - 1

    def next(self):  # O(1)
        self.pointer += 1
        return self.arr[self.pointer]

    def hasPrev(self):  # O(1)
        return self.pointer > 0

    def prev(self):  # O(1)
        self.pointer -= 1
        return self.arr[self.pointer]