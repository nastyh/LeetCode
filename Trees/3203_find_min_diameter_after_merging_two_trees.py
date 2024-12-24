class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        """
        O(n+m), where n and m are the numbers of nodes in the trees. BFS visits all of them
        O(n+m) same due to the adj lists, BFS deque, and such

        diameter is the longest path b/w the two nodes in the tree
        when a path starts in one tree and ends in another, we need to somehow
        get the centroids of the trees 
        Centroid of a tree is a node which if removed from the tree would split it
        into a ‘forest’, such that any tree in the forest would have at most half the number of vertices in the original tree.
        the combined diameter of the tree is the sum of the halves of the original diameters plus one for the extra edge:
        d1/2 + d2/2 + 1

        Calculate the number of nodes for each tree:
        uild adjacency lists for both trees
        Calculate the diameters of both trees:
        Calculate the longest path that spans across both trees, combined_d
        Return the maximum of the three possibilities: max(d1, d2, combined_d)
        """
        def build_adj_list(size, edges):
            """
            input is the list of lists, has size lists inside
            adj list is [first element, second element] and vice versa
            """
            adj_list = [[] for _ in range(size)]
            for edge in edges:
                adj_list[edge[0]].append(edge[1])
                adj_list[edge[1]].append(edge[0])
            return adj_list

        def find_farthest_node(n, adj_list, source_node):
            queue = deque([source_node])
            visited = [False] * n
            visited[source_node] = True

            maximum_distance = 0
            farthest_node = source_node
            while queue:
                for _ in range(len(queue)):
                    current_node = queue.popleft()
                    farthest_node = current_node

                    for neighbor in adj_list[current_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                if queue:
                    maximum_distance += 1
            return farthest_node, maximum_distance

        def find_diameter(n, adj_list):
            # First BFS to find the farthest node from an arbitrary node (e.g., 0)
            farthest_node, _ = find_farthest_node(n, adj_list, 0)

        # Second BFS to find the diameter starting from the farthest node
            _, diameter = find_farthest_node(n, adj_list, farthest_node)
            return diameter

        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists for both trees
        adj_list1 = build_adj_list(n, edges1)
        adj_list2 = build_adj_list(m, edges2)

        # Calculate the diameters of both trees
        diameter1 = find_diameter(n, adj_list1)
        diameter2 = find_diameter(m, adj_list2)

        # Calculate the longest path that spans across both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combined_diameter)