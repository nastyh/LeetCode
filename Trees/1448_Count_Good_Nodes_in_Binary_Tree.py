from collections import deque
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def goodNodes(self, root):  # O(n) and O(h)
        """
        DFS approach
        Keep track of the current node and max_val. Max_val is the maximum node's value we've seen so far. All deeeper nodes should be >= than this value 
        in order to be considered a good node 
        """
        if not root: return 0
        if root and not root.left and not root.right: return 1 
        res = 0
        def _helper(node, max_val):
            nonlocal res
            if not node: return
            if node.val >= max_val:
                res += 1
            max_val = max(max_val, node.val)
            if node.left:
                _helper(node.left, max_val)
            if node.right:
                _helper(node.right, max_val)
        _helper(root, -math.inf)
        return res

    
    def goodNodes_bfs(self, root):
        """
        Same but using BFS 
        """
        if not root: return 0
        if root and not root.left and not root.right: return 1 
        res = 0
        d = deque()
        d.append((root, -math.inf))
        while d:
            t, max_val = d.popleft()
            if t.val >= max_val:
                res += 1
            max_val = max(max_val, t.val)
            if t.left:
                d.append((t.left, max_val))
            if t.right:
                d.append((t.right, max_val))
        return res 

        
    def goodNodes_iter(self, root):
        stack = [(root, root.val)]
        top = root
        count = 0
        while stack:
            temp = []
            while len(stack):
                node, parent = stack.pop()
                if node.val >= parent: count += 1
                if node.left: temp.append((node.left, max(parent, node.val)))
                if node.right: temp.append((node.right, max(parent, node.val)))
            stack = temp
        return count