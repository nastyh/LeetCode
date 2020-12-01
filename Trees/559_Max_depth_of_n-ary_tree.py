from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def maxDepth(self, root: Node) -> int:  # times out
        res = 0
        if not root:
            return 0
        levels = deque([root])
        while levels:
            curr = levels.popleft()
            res += 1
            if root.children:
                levels.append(root.children)
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



