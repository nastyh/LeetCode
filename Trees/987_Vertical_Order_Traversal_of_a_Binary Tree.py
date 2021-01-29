from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# append node, column, row to the queue.
# Create a dictionary: column: (row, node's value)
# Append node's values to list res after sorting each key (which is a list itself)

    def verticalTraversal_BFS(self, root): # BFS-based  O(nlogn) b/c of sorting and O(n) of the defaultdict
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
        return res


    def verticalTraversal_BFS_other(self, root):
        """
        Slightly different from above. 
        Build defaultdict in form of { col: [[row, val]] }
        Then we will unpack it in two steps
        First step: we will create a list of lists by_row that will contain dictionary's values (lists of lists)
        sorted by row and value
        Second step: iterate through every element inside by_row and extract the second element (value) of every element
        Store everything in res and return 
        """
        if not root: return None
        if root and not root.left and not root.right: return [root]
        d = defaultdict(list)
        q = deque()
        res = []
        q.append([0, 0, root])  # [col, row, val]
        while q: 
            for _ in range(len(q)):
                combo = q.popleft()
                col, row, t = combo[0], combo[1], combo[2]
                d[col].append([row, t.val])
                if t.left or t.right:
                    row += 1
                if t.left:
                    q.append([col - 1, row, t.left])
                if t.right:
                    q.append([col + 1, row, t.right])
        by_row = []
        for x in sorted(d.items(), key = lambda x: (x[0], x[1])):
            by_row.append(sorted(x[1]))
        for el in by_row:
            curr = []
            for node in el:
                curr.append(node[1])
            res.append(curr)
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
    m = TreeNode(1)
    m.left = TreeNode(2)
    m.right = TreeNode(3)
    m.left.left = TreeNode(4)
    m.left.right = TreeNode(5)
    m.right.left = TreeNode(6)
    m.right.right = TreeNode(7)
    # print(l.verticalTraversal_BFS(l))
    # print(l.verticalTraversal_DFS(l))
    print(m.verticalTraversal_BFS_other(m))
