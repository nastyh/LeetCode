from collections import defaultdict, deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        O(n + m + 26n) = O((n + m) * 26) due to per-node 26-color processing
        O(26n + m) for the dp table and graph.
        where n is number of nodes (len(colors)) and m is number of edges (len(edges))

        Detect cycles using Kahn's Algorithm (BFS-based topological sort).
        Track color counts per node along all paths using a 2D DP table
        dp[node][color] = max count of color c on any path ending at node.

        Build graph and in-degree array.
        Use Kahn’s algorithm to process nodes in topological order.
        For each node, for each neighbor:
          -- Update the neighbor's color counts from the current node.
          -- Reduce neighbor’s in-degree and add to queue if it becomes 0.
        Track the maximum value of any color during the process.
        If we process fewer nodes than n, it means there's a cycle ⇒ return -1.
        """
        d, degrees = defaultdict(list), [0] * len(colors)
        for start, end in edges:
            d[start].append(end)
            degrees[end] += 1

        dp = [[0] * 26 for _ in range(len(colors))]
        q = deque()

        for i in range(len(colors)):
            if degrees[i] == 0:
                q.append(i)
            # to map each character (from a to z to an integer from 0 to 25)
            dp[i][ord(colors[i]) - ord('a')] = 1 # ord(colors[i]) - ord('a') gives a 0-based index corresponding to this color

        visited, max_color_val = 0, 0

        while q:
            curr_n = q.popleft()
            visited += 1
            for neighbor in d[curr_n]:
                for c in range(26):
                    # dp[i][c] is the max number of times color c appears on any path ending at node i
                    # We initialize dp[i][<color of node i>] = 1 because any path ending at node i that only includes i will see that color once.
                    dp[neighbor][c] = max(dp[neighbor][c], dp[curr_n][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0))
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    q.append(neighbor)
            max_color_val = max(max_color_val, max(dp[curr_n]))
        return max_color_val if visited == len(colors) else -1

