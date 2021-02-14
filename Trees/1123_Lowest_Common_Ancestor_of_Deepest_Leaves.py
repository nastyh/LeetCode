# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def lcaDeepestLeaves(self, root):  # O(n) and O(n) in the worst case, but on average O(log(n))
        def helper(node):
            if not node:
                return [node, 0]
            if not node.left and not node.right:
                return [node, 0]

            if not node.right:
                left_node, left_dep = helper(node.left)
                return [left_node, left_dep + 1]

            if not node.left:
                right_node, right_dep = helper(node.right)
                return [right_node, right_dep + 1]

            left_node, left_dep = helper(node.left)
            right_node, right_dep = helper(node.right)
            if left_dep > right_dep:
                return [left_node, left_dep + 1]
            elif left_dep < right_dep:
                return [right_node, right_dep + 1]
            else:
                return [node, left_dep + 1]

        return helper(root)[0]

        # easier to understand

    def lcaDeepestLeaves_easy(self, root):
        def _helper(node):
            if not node:
                return (None, 0)
            l_node, l_depth = _helper(node.left)
            r_node, r_depth = _helper(node.right)

            if l_depth == r_depth:
                return (node, l_depth + 1)
            elif l_depth > r_depth:
                return (l_node, l_depth + 1)
            else:
                return (r_node, r_depth + 1)
        n, d = _helper(root)
        return n



if __name__ == '__main__':
    l = TreeNode(11)
    l.left = TreeNode(4)
    l.right = TreeNode(16)
    l.left.left = TreeNode(2)
    l.left.right = TreeNode(8)
    l.left.right.left = TreeNode(6)
    l.left.right.right = TreeNode(10)
    print(l.lcaDeepestLeaves_easy(l))
