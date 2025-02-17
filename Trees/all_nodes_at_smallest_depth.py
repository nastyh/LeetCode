"""
Find all the elements in tree which are at same level, where level is depth of smallest path from root to leaf
"""
from collections import deque


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def nodes_at_smallest_depth(self, root: TreeNode):
        if not root: return []
        if root and not root.left and not root.right:
            return [root.val]
        d = deque([root])
        while d:
            curr_level = []
            next_level = []
            res_found = False 
            for _ in range(len(d)):
                t = d.popleft()
                curr_level.append(t.val)
                if not t.left and not t.right:
                    res_found = True 
                if t.left:
                    next_level.append(t.left)
                if t.right:
                    next_level.append(t.right)
            if res_found:
                return curr_level
            d.extend(next_level)
        return []
    
    def nodes_at_smallest_depth_another(self, root: TreeNode):
        """
        O(n) both
        BFS
        process level by level. Once you see no children,
        we need to get the results of this level out 
        need the boolean so we have everything on this level saved 
        """
        if not root: return []
        if root and not root.left and not root.right:
            return [root.val]
        d = deque([root])
        while d:
            curr_level = []
            res_found = False 
            for _ in range(len(d)):
                t = d.popleft()
                curr_level.append(t.val)
                if not t.left and not t.right:
                    res_found = True 
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            if res_found:
                return curr_level
        return []
    