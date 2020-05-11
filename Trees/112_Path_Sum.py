# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        l = []
        if not root:
            return False
        if root and (not root.left and not root.right):
            return root.val == sum
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
    
from collections import deque   
    def hasPathSum_BFS(self, root: TreeNode, sum: int):
        if not root:
            return False
        q = deque()
        q.append([root, 0])
        
        while q:
            t = q.popleft()
            t[1] =+ t[0].val
            if (not t[0].left and not t[0].right):
                return t[1] == sum
            else:
                if t[0].left:
                    q.append([t[0].left, t[1]])
                if t[0].right:
                    q.append(t[0].right, t[1])
        return False
            
            
        