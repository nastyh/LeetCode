# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView_brute_force_bfs(self, root: Optional[TreeNode]) -> List[int]:
        """
        O(n) both
        BFS
        if we see the first element, save to res 
        """
        if root and not root.left and not root.right:
            return [root.val]
        if not root:
            return []
        res = []
        d = deque()
        d.append(root)
        while d:
           d_l = len(d)
           for i in range(d_l):
                curr_node = d.popleft()
                if i == 0:
                   res.append(curr_node.val)
                if curr_node.left:
                    d.append(curr_node.left)
                if curr_node.right:
                    d.append(curr_node.right)
        return res 
                   