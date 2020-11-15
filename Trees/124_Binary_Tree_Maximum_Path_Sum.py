import math
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    
    def maxPathSum_postorder(self, root):
        self.res = -math.inf
        def _helper(root):
            if not root:  return 0
            left_val, right_val = max(0, _helper(root.left)), max(0, _helper(root.right))
            self.res = max(self.res, (root.val + left_val + right_val))
            return max((root.val + left_val), (root.val + right_val))
        _helper(root)
        return self.res

    
    def maxPathSum_recur(self, root):
        self.res = -math.inf
        def _helper(root):
            if not root: return 0
            l = max(0, _helper(root.left))
            r = max(0, _helper(root.right))
            self.res = max(self.res, l + r + root.val)
            return max(l, r) + root.val
        _helper(root)
        return self.res


if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    m = TreeNode(-10)
    m.left = TreeNode(9)
    m.right = TreeNode(20)
    m.right.left = TreeNode(15)
    m.right.right = TreeNode(7)
    print(l.maxPathSum_postorder(l))
    print(m.maxPathSum_postorder(m))
    print(l.maxPathSum_recur(l))
    print(m.maxPathSum_recur(m))