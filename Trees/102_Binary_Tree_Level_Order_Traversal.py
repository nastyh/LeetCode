# Binary tree level order traversal
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]: # returns a list of list. Every level is a list
        if not root:
            return None
        
        res = []
        q = deque()
        
        q.append(root)
        
        while q:
            for _ in range(len(q)):
                values_in_level = []
                t = popleft()
                values_in_level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(values_in_level)
        return res
        