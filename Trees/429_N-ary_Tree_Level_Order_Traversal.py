from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        if not root: return 
        d, res = deque(), []
        d.append(root)
        while d:
            curr = []
            for _ in range(len(d)):           
                t = d.popleft()
                curr.append(t.val)
                for c in t.children:
                    d.append(c)
            res.append(curr)
        return res 
        