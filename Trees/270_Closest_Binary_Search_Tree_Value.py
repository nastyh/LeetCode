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


    def closestValue_efficient(self, root, target): # keeping track on the run
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

if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(5)
    l.left.left = TreeNode(1)
    l.left.right = TreeNode(3)
    print(l.closestValue(l, 3.714286))
    print(l.closestValue_efficient(l, 3.714286))

