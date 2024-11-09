# Definition for a binary tree node.
import math
# assumption: it returns the node's value, not the node itself.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def closestValue_dfs_recursion(self, root, target): 
        self.res = float('inf')
        def _helper(node):
            if not node: return 
            if abs(node.val - target) < abs(self.res - target):
                self.res = node.val
            elif abs(node.val - target) == abs(self.res - target):
                self.res = min(self.res, node.val)  #  If there are multiple answers, print the smallest.
            if target < node.val:
                _helper(node.left)
            if target > node.val:
                _helper(node.right)
        _helper(root)
        return self.res

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


    def closestValue_binary(self, root, target):  # binary search in a recursive manner  O(h) and O(1)
        """
        go left if target is smaller than current root value, and go right otherwise.
        Choose the closest to target value at each step.
        """
        ans = float("inf")
        while root:
            if root.val == target: return root.val
            ans = min(ans, root.val, key = lambda x: abs(x - target))
            if root.val > target: root = root.left
            else: root = root.right
        return ans

    
    def closestValue_trav(self, root, target):  # O(n) both 
        """
        Early stopping of a list traversal
        Traverse the tree in a pre-order fashion. Get a list in a sorted order
        Start iterating and calculating the differences. 
        Possible patterns are:
        1) first element is the closest. Difference is increasing. We do an early stopping. 
        2) valley pattern. Difference is decreasing, than starts increasing. In this case we do an early stopping after seeing that it starts increasing 
        3) last element is the closest. Difference is decreasing all the way. We keep updating min_diff and at the end return ans 
        """
        nums = []
        min_diff = math.inf
        def _trav(node):
            if not node: return 
            _trav(node.left)
            nums.append(node.val)
            _trav(node.right)
        _trav(root)
        for num in nums:
            curr_diff = abs(target - num)
            if curr_diff < min_diff:
                min_diff = curr_diff
                ans = num
            else:
                return ans
        return ans


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(5)
    l.left.left = TreeNode(1)
    l.left.right = TreeNode(3)
    # print(l.closestValue(l, 3.714286))
    # print(l.closestValue_efficient(l, 3.714286))
    print(l.closestValue_binary(l, 3.714286))
    print(l.closestValue_trav(l, 3.714286))
