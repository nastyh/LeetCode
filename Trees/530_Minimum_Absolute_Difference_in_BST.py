# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def getMinimumDifference(self, root):
        def get_values(values, root):
            if root is not None:
                values.append(root.val)
                values = get_values(values, root.left)
                values = get_values(values, root.right)
            return values

        values_list = get_values([], root)

        if len(values_list) != len(set(values_list)):
            return 0

        values_list.sort()
        minimum_diff = values_list[1] - values_list[0]

        for i in range(1, len(values_list)):
            diff = values_list[i] - values_list[i - 1]
            if diff < minimum_diff:
                minimum_diff = diff

        return minimum_diff

if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(3)
    l.right.right = TreeNode(2)
    print(l.getMinimumDifference(l))
