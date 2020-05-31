# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBalanced(self, root):
        def _helper(node):
            if not node: return 0
            return max(1 + _helper(node.left), 1 + _helper(node.right))

        if not root: return True
        else:
            l = _helper(root.left)
            r = _helper(root.right)
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(l - r) <= 1







    def isValidBST(self, root):
        if not root: return True
        if root and not root.left and not root.right: return True

        def _helper(node, lo = -math.inf, hi = math.inf):
            if not node:
                return True
            if node.val < lo or node.val > hi:
                return False

            return _helper(node.left, -math.inf, node.val) and _helper(node.right, node.val, math.inf)

        return _helper(root)

        # another working
        # if not root: return True
        # if root and not root.left and not root.right: return True

        # def _helper(node, lo, hi):
        #     if node:
        #         if node.val <= lo or node.val >= hi:
        #             return False
        #         return _helper(node.left, lo, node.val) and _helper(node.right, node.val, hi)
        #     return True

        # return _helper(root, -math.inf, math.inf)


        # iteratively:
    def isValidBST_iter(self, root):
        if not root: return True
        st = []

        st.append((root, -math.inf, math.inf))
        while st:
            node, l, r = st.pop()
            if node.val < l or node.val > r:
                return False
            if node.left:
                st.append((node.left, l, node.val))
            if node.right:
                st.append((node.right, node.val, r))
        return True





if __name__ == '__main__':
    l = TreeNode(7)
    l.left = TreeNode(3)
    l.right = TreeNode(9)
    l.right.left = TreeNode(8)
    l.right.right = TreeNode(12)
    l.right.right.right = TreeNode(16)
    # print(l.isValidBST(l))
    # print(l.isValidBST_iter(l))
    print(l.isBalanced(l))

    m = TreeNode(1)
    m.left = TreeNode(2)
    m.right = TreeNode(2)
    m.left.left = TreeNode(3)
    m.left.right = TreeNode(3)
    m.left.left.left = TreeNode(4)
    m.left.left.right = TreeNode(4)
    print(m.isBalanced(m))
