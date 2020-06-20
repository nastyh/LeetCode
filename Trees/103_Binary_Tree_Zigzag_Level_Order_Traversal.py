#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Printing out by level: one level left to right, another right to left, etc.

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def zigzagLevelOrder(self, root):
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

    def zigzagLevelOrder_alt(self, root):
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
                values_in_level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(values_in_level)
        return [v if k % 2 == 0 else v[::-1] for k,v in enumerate(res)]



if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)
    print(l.zigzagLevelOrder(l))
    print(l.zigzagLevelOrder_alt(l))
        