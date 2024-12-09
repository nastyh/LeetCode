"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        O(n^2) since n^2 cells to check in total
        O(logn) to store the recursive stack
        Recursively construct the quadtree. Given some grid, we divide
        it into 4 subgrids, construct the nodes for those subgrids, then
        combine those children nodes into a tree. These base case is when
        we reach a grid of size 1, we know this must be a leaf node.
        If all children are leaves and they all have the same val, then the current grid contains all the same values
        If one of the children is not a leaf, then that subgrid contains multiple values.
        If all children are leaves but their values differ, then the grid contains different values.
        In these cases, we create a parent node and connect them to each child.
        """
        def _helper(top, left, l):
            if l == 1:
                return Node(grid[top][left], True)
            topLeft = _helper(top, left, l // 2)
            topRight = _helper(top, left + l // 2, l // 2)
            botLeft = _helper(top + l // 2, left, l // 2)
            botRight = _helper(top + l // 2, left + l // 2, l // 2)

            children = [topLeft, topRight, botLeft, botRight]
            # Check if all subgrids have the same value
            if all(child.isLeaf and child.val == topLeft.val for child in children):
                return Node(topLeft.val, True)
            return Node(0, False, topLeft, topRight, botLeft, botRight)
        
        return _helper(0, 0, len(grid))


    def construct_another(self, grid: List[List[int]]) -> 'Node':
        """
        Cleaner than the previous but the same idea
        """

        def _helper(grid: List[List[int]]) -> bool:
            # shows whether it's a leaf
            return all(value == grid[0][0] for row in grid for value in row) 
        
        n = len(grid)
        if _helper(grid):
            return Node(grid[0][0], True)
        
        top_left_node = self.construct_another([row[:n//2] for row in grid[:n//2]])
        top_right_node = self.construct_another([row[n//2:] for row in grid[:n//2]])
        bottom_left_node = self.construct_another([row[:n//2] for row in grid[n//2:]])
        bottom_right_node = self.construct_another([row[n//2:] for row in grid[n//2:]])

        return Node(0, False, top_left_node, top_right_node, bottom_left_node, bottom_right_node)