from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
        O(n+m+q), n num of nodes in the graph, m edges, q queries 
        O(n)

        suppose the two nodes belong to the same connected component.
        What is the minimum cost of a walk connecting them? As mentioned,
        the optimal walk includes as many edges as possible.
        Since revisiting an edge does not affect the total score,
        we can freely traverse the edges of the component, meaning that we can move back and forth to reach all of them.
        Therefore, the best way to achieve the lowest cost is to visit every edge in the component.
        we use the Disjoint Set (Union-Find) data structure.
        This approach relies on two main operations: Union and Find.
        Each connected component has a representative node, known as its root,
        which is returned by the Find operation for any node in the group.
        When we Union two nodes, we merge their entire groups, as now a path exists between every node in one group and every node in the other. To maintain efficiency, the root of the larger group is chosen as the representative of the merged group. This minimizes the time needed for future Find operations by reducing the number of steps required to reach the current representative.
        """
        parent = [-1] * n
        depth = [0] * n 
        component_cost = [-1] * n 
        res = []
        
        def _helper(node):  # it's a find step
            if parent[node] == -1:
                return node 
            parent[node] = _helper(parent[node])
            return parent[node]
        def _union(n1, n2):  # it's a union step
            root1 = _helper(n1)
            root2 = _helper(n2)
            if root1 == root2:
                return 
            if depth[root1] < depth[root2]:
                root1, root2 = root2, root1
            parent[root2] = root1 
            if depth[root1] == depth[root2]:
                depth[root1] += 1

        for edge in edges:
            _union(edge[0], edge[1])
        for edge in edges:
            root = _helper(edge[0])
            component_cost[root] &= edge[2]

        for query in query:
            st, end  = query
            if _helper(st) != _helper(end):
                res.append(-1)
            else:
                root = _helper(st)
                res.append(component_cost[root])
        return res         
            