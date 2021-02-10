#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSubtree(self, s, t):  # O(mn) both  
        def _isEqual(a, b):
        if not a and not b:
            return True
        if a and not b:
            return False
        if not a and b:
            return False
        if a.val != b.val:
            return False            
        return _isEqual(a.left, b.left) & _isEqual(a.right, b.right)
    
        if not s and not t:
        return True
        if s and not t:
        return False
        if not s and t:
        return False 
        if _isEqual(s, t):
        return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    

