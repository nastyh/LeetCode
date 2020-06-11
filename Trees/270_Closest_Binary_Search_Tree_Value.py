# Definition for a binary tree node.
import math
# assumption: it returns the node's value, not the node itself.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def closestValue(self, root, target):  # creating a list of lists where the first element is node's values, the second is the difference
        st, res = [], []
        st.append(root)
        while st:
            el = []
            curr_node = st.pop()
            curr_diff = abs(curr_node.val - target)
            el.append(curr_node.val)
            el.append(curr_diff)
            if curr_node.left:
                st.append(curr_node.left)
            if curr_node.right:
                st.append(curr_node.right)
            res.append(el)
        res_sorted = sorted(res, key = lambda x: x[1]) # sorting the list of lists by the second value (by the difference) and returning the node value with such difference
        return res_sorted[0][0]

    def closestValue_efficient(self, root, target): # keeping track on the go
        st, glob_diff, glob_node = [], math.inf, None
        st.append(root)
        while st:
            curr_node = st.pop()
            curr_diff = abs(curr_node.val - target)
            if glob_diff > curr_diff:
                glob_diff = curr_diff
                glob_node = curr_node.val
            if curr_node.left:
                st.append(curr_node.left)
            if curr_node.right:
                st.append(curr_node.right)
        return glob_node

    def closestValue_dfs2(self, root, target): # DFS but with outside variables. Avoid if you can
        self.diff = math.inf
        self.res = 0

        def _helper(root, target, diff, res):
            if not root: return
            if self.diff >= abs(root.val - target):
                self.diff = abs(root.val - target)
                self.res = root.val
            _helper(root.left, target, self.diff, self.res)
            _helper(root.right, target, self.diff, self.res)

        _helper(root, target, self.diff, self.res)
        return self.res


    def closestValue_binary(self, root, target):
        ans = float("inf")
        while root:
            if root.val == target: return root.val
            ans = min(ans, root.val, key=lambda x: abs(x-target))
            if root.val > target: root = root.left
            else: root = root.right
        return ans


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(5)
    l.left.left = TreeNode(1)
    l.left.right = TreeNode(3)
    # print(l.closestValue(l, 3.714286))
    # print(l.closestValue_efficient(l, 3.714286))
    print(l.closestValue_dfs2(l, 3.714286))
    # print(l.closestValue_binary(l, 3.714286))
