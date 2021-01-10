# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def deepestLeavesSum(self, root):  # O(h) and O(h), where h is the tree's height
        """
        Step 1: find max depth of the tree
        Step 2: traverse the tree in a DFS manner and keep track of the current depth
        If current depth == max depth, add the node's value to res 
        """
        if root and not root.left and not root.right: return root.val
        def _find_max_depth(node):
            if not node: return 
            if node and not node.left and not node.right:
                return 1
            if node.left:
                l = _find_max_depth(node.left) + 1
            else:
                l = 0
            if node.right:
                r = _find_max_depth(node.right) + 1
            else:
                r = 0
            return max(l, r)
        max_depth = _find_max_depth(root)
        res = 0
        def _trav(node, d, max_depth):
            nonlocal res
            if not node:
                return 
            if d == max_depth:
                res += node.val
            if node.left:
                _trav(node.left, d + 1, max_depth)
            if node.right:
                _trav(node.right, d + 1, max_depth)
        _trav(root, 1, max_depth)
        return res


    def deepestLeavesSum_BFS(self, root):  # O(N) to visit each node and O(N) to keep the queue in the worst case 
        """
        Step 1: is the same
        Step 2: traverse the tree in a BFS manner and keep track of the current depth 
        """
        def _find_max_depth(node):
            if not node: return 
            if node and not node.left and not node.right:
                return 1
            if node.left:
                l = _find_max_depth(node.left) + 1
            else:
                l = 0
            if node.right:
                r = _find_max_depth(node.right) + 1
            else:
                r = 0
            return max(l, r)
        max_depth = _find_max_depth(root)
        d = deque()
        res = 0
        d.append((root, 1))
        while d:
            for _ in range(len(d)):
                t, curr_depth = d.popleft()
                if curr_depth == max_depth:
                    res += t.val
                if t.left or t.right:
                    curr_depth += 1
                if t.left:
                    d.append((t.left, curr_depth))
                if t.right:
                    d.append((t.right, curr_depth))
        return res

    
    def deepestLeavesSum_BFS_alt(self, root):  # O(N) to visit each node and O(N) to keep the queue in the worst case 
        """
        Just calculate the sum of the level from scratch for every level. 
        At the end, you'll end up with the sum of the lowest level 
        """
        d, res = deque(), 0
        d.append(root)
        while d:
            res = 0
            for _ in range(len(d)):
                t = d.popleft()
                res += t.val
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
        return res 