# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
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
