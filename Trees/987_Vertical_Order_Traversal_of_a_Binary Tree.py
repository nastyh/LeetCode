
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# append node, column, row to the queue.
# Create a dictionary: column: (row, node's value)
# Append node's values to list res after sorting each key (which is a list itself)

    def verticalTraversal_BFS(self, root): # BFS-based
        if not root: return None
        d = defaultdict(list)
        min_col, max_col = 0, 0
        q = deque()
        q.append([root, 0, 0]) # order is node, col, row

        while q:
            t, col, row = q.popleft()
            d[col].append((row, t.val))
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            if t.left or t.right:
                row += 1
            if t.left:
                q.append([t.left, col - 1, row])
            if t.right:
                q.append([t.right, col + 1, row])
        res = []
        for c in range(min_col, max_col + 1):
            res.append([val for row, val in sorted(d[c])])
        # return d
        return res

    def verticalTraversal_DFS(self, root): # DFS applied to filling the dictionary
        if not root: return None
        d = defaultdict(list)
        min_col, max_col = 0, 0

        def _helper(root, row, col):
            if root:
                nonlocal min_col, max_col
                d[col].append((row, root.val))
                min_col = min(col, min_col)
                max_col = max(col, max_col)

                _helper(root.left, row + 1, col - 1)
                _helper(root.right, row + 1, col + 1)

        _helper(root, 0, 0)
        res = []
        for c in range(min_col, max_col + 1):
            res.append([val for row, val in sorted(d[c])])
    # return d
        return res





if __name__ == '__main__':
    l = TreeNode(7)
    l.left = TreeNode(3)
    l.right = TreeNode(11)
    l.left.left = TreeNode(1)
    l.right.left = TreeNode(2)
    l.left.right = TreeNode(9)
    l.right.right = TreeNode(14)
    print(l.verticalTraversal_BFS(l))
    print(l.verticalTraversal_DFS(l))
