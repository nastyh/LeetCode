class Solution:
    def allPathsSourceTarget_bfs(self, graph: List[List[int]]) -> List[List[int]]:  # O(c^n) where c is the num of children and O(n)
        """
        find all possible paths from node 0 to node n-1 for a DAG.
        ll possible paths means that all paths are correct and there are not any incorrect paths.
        """
        res = []
        q = collections.deque([(0,[])])
        while q:
            node, path = q.popleft()
            if node == len(graph) - 1: # made it to the final node 
                res.append(path + [node])
            for child in graph[node]:  # keep it running 
                q.append([child, path + [node]])
        return res

    def allPathsSourceTarget_dfs(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def _helper(node, path):
            if node == n - 1: 
                res.append(path)
                return 
            for next_node in graph[node]:
                _helper(next_node, path + [next_node])
        _helper(0, [0])
        return res

