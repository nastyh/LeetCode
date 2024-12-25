from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def maxDepth_dfs(self, root: 'Node') -> int:
        """
        O(n) both
        DFS, recursive 
        """
        if not root: return 0
        res = 0
        for child in root.children:
            res = max(res, self.maxDepth(child))
        return res + 1
    
    def maxDepth_bfs(self, root: 'Node') -> int:
        """
        O(n) both
        Normal BFS
        add (node, level) to the deque
        if there is a child, add it, increase the level
        keep track of the abs best result in res 
        """
        if not root: return 0
        d = deque()
        res = -math.inf
        d.append((root, 1))
        while d:
            t, curr_depth = d.popleft()
            res = max(res, curr_depth)
            for ch in t.children:
                d.append((ch, curr_depth + 1))
        return res 


    def maxDepth_dfs(self, root):  # works
        if not root:
            return 0
        if not root.children:
            return 1
        levels = []
        for node in root.children:
        levels.append(self.maxDepth(node))
        return max(levels) + 1



