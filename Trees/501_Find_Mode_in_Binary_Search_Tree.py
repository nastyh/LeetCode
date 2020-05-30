# Definition for a binary tree node.
import statistics
# from statistics import multimode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def findMode(self, root):
        if not root: return []
        li = []

        def _helper(node, li):
            if not node:
                return
            _helper(node.left, li)
            li.append(node.val)
            _helper(node.right, li)
            return li

        out = _helper(root, li)
        # return statistics.multimode(out)
        return statistics.mode(out)



if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(2)
    l.right.left = TreeNode(2)
    print(l.findMode(l))
