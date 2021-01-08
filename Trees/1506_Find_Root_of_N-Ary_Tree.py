# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree):  # O(n) both
        seen = set()
        for node in tree:
            for child in node.children:
                seen.add(child.val)
        for node in tree:
            if node.val not in seen:
                return node


class Solution:
    def findRoot(self, tree):  # O(n) and O(1)
        """
        for some reason, it looks like a, b, c, b, a
        If you add and then subtract all numbers that appear twice, you'll end up with the number 
        that appears once, it will be the root 
        """
        value_sum = 0
        for node in tree:
            # the value is added as a parent node
            value_sum += node.val
            for child in node.children:
                # the value is deducted as a child node.
                value_sum -= child.val
        # the value of the root node is `value_sum`
        for node in tree:
            if node.val == value_sum:
                return node


class Solution:  # same as above but with XOR
    def findRoot(self, tree):
        ans = 0
        for x in tree:
            ans = ans ^ x.val
            for ch in x.children:
                ans = ans ^ ch.val
        for node in tree:
            if node.val == ans:
                return node