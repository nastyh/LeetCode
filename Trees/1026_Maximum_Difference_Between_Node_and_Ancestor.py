import math
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right


def maxAncestorDiff(self, root):  # O(n) both 
    def _helper(root, curr_min = math.inf, curr_max = -math.inf):
        """
        Curr node's value and against what we're comparing it 
        """
        curr_max = max(root.val, curr_max)
        curr_min = min(root.val, curr_min)
        result = abs(curr_max - curr_min)
        if root.left:
            result = max(result, _helper(root.left, curr_min, curr_max))
        if root.right:
             result = max(result, _helper(root.right, curr_min, curr_max))
        return result
    return _helper(root, math.inf, -math.inf)
    

def maxAncestorDiff_another(self, root):
    max_diff = -float('inf')
    def dfs(root, path):
        nonlocal max_diff
        if not root:
            # print(path)
            max_diff = max(max_diff, max(path) - min(path))
            return
        dfs(root.left, path + [root.val])
        dfs(root.right, path + [root.val])
    dfs(root, [])
    return max_diff


def maxAncestorDiff_iter(self, root):
    stack = [[root, root.val, root.val]]
    ans = 0
    while stack:
        node, curr_min, curr_max = stack.pop()
        ans = max(ans, abs(node.val-curr_min), abs(node.val-curr_max))
        curr_min = min(curr_min, node.val)
        curr_max = max(curr_max, node.val)
        if node.left:
            stack.append([node.left, curr_min, curr_max])
        if node.right:
            stack.append([node.right, curr_min, curr_max])
    return ans