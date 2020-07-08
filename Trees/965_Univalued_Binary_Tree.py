from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isUnivalTree(self, root): # recursively
        if not root: return True
        if root and not root.left and not root.right: return True
        def _helper(root, val):
            if not root: return True
            if root.val != val:
                return False
            l = _helper(root.left, root.val)
            r = _helper(root.right, root.val)
            return l & r
        return _helper(root, root.val)

    def isUnivalTree_BFS(self, root): # BFS
         if not root: return True
        d = deque()
        d.append(root)
        res = []
        while d:
            t = d.popleft()
            res.append(t.val)
            if t.left:
                d.append(t.left)
            if t.right:
                d.append(t.right)
        return len(set(res)) == 1
        
        