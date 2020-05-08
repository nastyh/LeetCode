"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res, s = [], []
        if not root:
            return None
        s.append(root)
        while s:
            t = s.pop()
            if t:
                res.append(t.val)
                for i in range(len(t.children)-1, -1, -1):
                    s.append(t.children[i])
        return res
