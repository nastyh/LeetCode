def splitBST(root, V):
    target = None
    def find(root):
        nonlocal target, V
        if not root:
            return
        if root.val <= V:
            target = root
            find(root.right)
        else:
            find(root.left)

    def findPath(root):
        nonlocal target
        if not root:
            return
        path.append(root)
        if root.val < target.val:
            findPath(root.right)
        elif root.val > target.val:
            findPath(root.left)
        else:
            return
    
    find(root)
    if target == None:
        return None, root
    path = []
    
    findPath(root)

    left, right, left.right = path[-1], path[-1].right, None
    while len(path) > 1:
        n = path.pop()
        if path[-1].val < n.val:
            path[-1].right = left
            left = path[-1]
        else:
            path[-1].left = right
            right = path[-1]
    return left, right