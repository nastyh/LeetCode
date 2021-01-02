# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def getTargetCopy(self, original, cloned, target):  # O(h) both
        """
        just recursive preorder traversal
        """
        if not original: return None
        ans = None
        def _helper(node, cloned, target):
            nonlocal ans
            if not node: return
            if node.val == target.val:
                ans = cloned
            if node.left:
                _helper(node.left, cloned.left, target)
            if node.right:
                _helper(node.right, cloned.right, target)
            return ans
        _helper(original, cloned, target)
    

    def getTargetCopy_BFS(self, original, cloned, target):  # O(N) both
        """
        Normal BFS.
        """
        if not original: return None
        d_orig, d_cloned = deque(), deque()
        d_orig.append(original)
        d_cloned.append(cloned)
        while d_orig:
            orig_val, cloned_val = d_orig.popleft(), d_cloned.popleft()
            if orig_val.val == target.val:
                return cloned_val
            if orig_val.left:
                d_orig.append(orig_val.left)
                d_cloned.append(cloned_val.left)
            if orig_val.right:
                d_orig.append(orig_val.right)
                d_cloned.append(cloned_val.right)

    
    def getTargetCopy_BFS_alt(self, original, cloned, target):  # O(N) both
        """
        Same as above but one deque
        """
        if not original: return None
        d = deque()
        d.append((original, cloned))
        while d:
            orig_val, cloned_val = d.popleft()
            if orig_val.val == target.val:
                return cloned_val
            if orig_val.left:
                d.append((orig_val.left, cloned_val.left))
            if orig_val.right:
                d.append((orig_val.right, cloned_val.right))


    def getTargetCopy_stack(self, original, cloned, target):  # O(N) both
        if not original: return None
        st = []
        st.append((original, cloned))
        while st:
            orig_val, cloned_val = st.pop()
            if orig_val.val == target.val:
                return cloned_val
            if orig_val.left:
                st.append((orig_val.left, cloned_val.left))
            if orig_val.right:
                st.append((orig_val.right, cloned_val.right))
