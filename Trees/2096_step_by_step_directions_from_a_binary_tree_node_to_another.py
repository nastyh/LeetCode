class Solution:
    def getDirections_graph(self, root: Optional[TreeNode], start: int, dest: int) -> str:
        """
        O(n)
        O(n^2): queue can have O(n) elements, and each element can have O(n) string each
        Traverse the tree once, and represent the tree as a graph with left, right and parent neighbours.
        Then just do a BFS from start node to find the shortest path to destination.
        """
        graph = defaultdict(lambda: [None, None, None])
        def dfs(root, par):
            if root.left:
                graph[root.val][0] = root.left.val
                dfs(root.left, root)
            if root.right: 
                graph[root.val][1] = root.right.val
                dfs(root.right, root)
            if par:
                graph[root.val][2] = par.val
        
        def bfs(start, dest):
            q = deque()
            q.append((start, ""))
            step = ["L", "R", "U"]
            visited = set()
            while q:
                node, path = q.popleft()
                if node == dest:
                    return path
                visited.add(node)
                for i, nei in enumerate(graph[node]):
                    if nei and nei not in visited:
                        q.append((nei, path + step[i]))
                        
        dfs(root, None)
        return bfs(start, dest)

    def getDirections_another(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        O(n)
        """
        def _helper(node, find_val, path):
            if node.val == find_val:
                return True
            if node.left and _helper(node.left, find_val, path):
                path += "L"
            elif node.right and _helper(node.right, find_val, path):
                path += "R"
            return path
        s, d = [], []
        _helper(root, startValue, s)
        _helper(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))
