#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Printing out by level: one level left to right, another right to left, etc.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res, level = [], 0 
        q = deque()
        q.append(root)
        while q:
            values_in_level = []
            level += 1
            for _ in range(len(q)):             
                t = q.popleft()
                values_in_level.append(t.val) if level % 2 == 1 else values_in_level.insert(0, t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(values_in_level)
        return res
        
        