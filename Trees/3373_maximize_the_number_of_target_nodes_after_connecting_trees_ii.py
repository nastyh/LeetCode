from collections import deque, defaultdict
from typing import List

class Solution:
    def maxTargetNodes_dfs(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """
        O(n+m) both, numbers of nodes in edges1 and edges2 since we need to visit each once 
        and then we store the color of each node 

        For the i-th query, after joining the two trees, the answer has two parts:
        The number of nodes in the first tree that are an even distance from node i.
        The number of nodes in the second tree that are an even distance from node i
        To retrieve these counts quickly, we first color each tree with depth-first search:
        assign the root color 0 (white); every node at an even distance from the root also gets color 0,
        and every node at an odd distance gets color 1 (black). We record the total number of white and black nodes.
        For any node, the number of its target nodes equals the number of nodes that share its color.

        """
        def dfs(node, parent, depth, children, color):
            res = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, depth + 1, children, color)
            return res

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = dfs(0, -1, 0, children, color)
            return [res, n - res]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        res = [0] * n
        for i in range(n):
            res[i] = count1[color1[i]] + max(count2[0], count2[1])
        return res
        
    def maxTargetNodes_bfs(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """
        assign parity (color) to each node.
        for each node in Tree1, compute
        Number of nodes in Tree1 that share its parity (i.e., are at even distance from it)
        Plus the maximum of the two parity groups in Tree2, since we can connect to either
        """
        def build_tree(n, edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        def bfs_color(tree, n):
            color = [-1] * n
            counts = [0, 0]  # color 0: even depth, color 1: odd depth
            q = deque([(0, 0)])
            while q:
                node, c = q.popleft()
                if color[node] != -1:
                    continue
                color[node] = c
                counts[c] += 1
                for nei in tree[node]:
                    if color[nei] == -1:
                        q.append((nei, 1 - c))
            return color, counts

        n = len(edges1) + 1
        m = len(edges2) + 1

        tree1 = build_tree(n, edges1)
        tree2 = build_tree(m, edges2)

        color1, count1 = bfs_color(tree1, n)
        color2, count2 = bfs_color(tree2, m)

        res = []
        for i in range(n):
            same_parity_in_tree1 = count1[color1[i]]
            max_parity_in_tree2 = max(count2[0], count2[1])
            res.append(same_parity_in_tree1 + max_parity_in_tree2)
        return res

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """
        TIMES OUT
        O(n^2+m)
        """
        def build_tree(edges, n):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        def get_parity_counts(tree, root):
            visited = set()
            q = deque([(root, 0)])
            parity = [0, 0]
            while q:
                node, depth = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                parity[depth % 2] += 1
                for nei in tree[node]:
                    if nei not in visited:
                        q.append((nei, depth + 1))
            return parity

        def get_even_counts_for_tree1(tree1, n):
            even_counts = [0] * n
            for i in range(n):
                visited = set()
                q = deque([(i, 0)])
                count = 0
                while q:
                    node, dist = q.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    if dist % 2 == 0:
                        count += 1
                    for nei in tree1[node]:
                        if nei not in visited:
                            q.append((nei, dist + 1))
                even_counts[i] = count
            return even_counts

        n = len(edges1) + 1
        m = len(edges2) + 1

        tree1 = build_tree(edges1, n)
        tree2 = build_tree(edges2, m)

        even2, odd2 = get_parity_counts(tree2, 0)
        even1_list = get_even_counts_for_tree1(tree1, n)

        res = []
        for i in range(n):
            # Tree1 even distances from i, Tree2 can be chosen to match parity
            res.append(even1_list[i] + max(even2, odd2))
        return res