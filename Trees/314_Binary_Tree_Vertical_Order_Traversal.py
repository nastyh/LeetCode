from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def verticalOrder_d(self, root): # BFS with a dictionary
        if not root: return None
        d = defaultdict(list)
        min_col, max_col = 0, 0
        q = deque()
        q.append([root, 0])

        while q:
            t, col = q.popleft()
            d[col].append(t.val)
            min_col = min(col, min_col)
            max_col = max(col, max_col)

            if t.left:

                q.append([t.left, col - 1])
            if t.right:

                q.append([t.right, col + 1])
        return [d[x] for x in range(min_col, max_col + 1)]

    
    def verticalOrder_d_clean(self, root):  # the best one; without min_col and max_col. Solved with sorted in the return statement
        if not root: return None
        d = defaultdict(list)
        q = deque()
        q.append([root, 0])
        while q:
            t, col = q.popleft()
            d[col].append(t.val)
            if t.left:
                q.append([t.left, col - 1])
            if t.right:
                q.append([t.right, col + 1])
        return [v for k, v in sorted(d.items())]


    def verticalOrder_dfs(self, root): # DFS with a dictionary
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret



    def verticalOrder(self, root): # returns a list of lists that is impossible to get results from
        row, col, d, res = 0, 0, deque(), []
        if not root: return None

        d.append((row, col, root))
        while d:
            curr_info = []
            min_col, max_col = 0, 0
            for _ in range(len(d)):

                curr_row, curr_col, t = d.popleft()
                curr_info.append((curr_row, curr_col, t.val))
                if t.left or t.right:
                    curr_row += 1
                if t.left:
                    min_col = min(curr_col, min_col)
                    d.append((curr_row, curr_col - 1, t.left))
                if t.right:
                    max_col = max(curr_col, max_col)
                    d.append((curr_row, curr_col + 1, t.right))
                # curr_row += 1
            res.append(curr_info)
        return res

if __name__ == '__main__':
    l = TreeNode(7)
    l.left = TreeNode(3)
    l.right = TreeNode(11)
    l.left.left = TreeNode(1)
    l.right.left = TreeNode(2)
    l.left.right = TreeNode(9)
    l.right.right = TreeNode(14)
    print(l.verticalOrder_d(l))
    print(l.verticalOrder_d_clean(l))
    print(l.verticalOrder_dfs(l))
    # print(l.verticalOrder(l))


