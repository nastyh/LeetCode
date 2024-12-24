class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        """
        O(m+n), source/target
        O(mn) prob for dp but one dimension is only 26, so it's O(m)
        treat the chars as the nodes in a graph
        Each transformation from original[i] to changed[i] with cost cost[i] represents a
        directed, weighted edge between nodes.
        Use the Floyd-Warshall algorithm to compute the shortest paths between all pairs of nodes.
        This algorithm is suitable since the number of nodes (26 lowercase English letters) is small.
        Initialize the graph with direct transformation costs. If no direct transformation exists
        between two characters, initialize the cost to a large number
        For each character in the source string, check the cost to convert it
        to the corresponding character in the target string using the shortest paths computed.
        Sum these costs. If any conversion is not possible (cost remains infinity), return -1.

        a 2D list dist to represent the cost of transforming any character to any other character.
        populate with provided transformation costs
        compute the shortest paths between all pairs of characters efficiently.
        """
        n = len(source)
        INF = float('inf')
        NUM_LETTERS = 26
        dp = [[INF] * NUM_LETTERS for _ in range(NUM_LETTERS)]
        #costs nothing to transform to itself: the diagonals
        for i in range(NUM_LETTERS):
            dp[i][i] = 0

        # Populate the cost matrix with the given transformation costs
        for o, c, z in zip(original, changed, cost):
            dp[ord(o) - ord('a')][ord(c) - ord('a')] = min(dp[ord(o) - ord('a')][ord(c) - ord('a')], z)
        
        # finding the shortest path
        for k in range(NUM_LETTERS):
            for i in range(NUM_LETTERS):
                for j in range(NUM_LETTERS):
                    if dp[i][k] < INF and dp[k][j] < INF:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        # minimum cost to transform source to target
        res = 0
        for s_char, t_char in zip(source, target):
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if dp[s_idx][t_idx] == INF:
                return -1
            res += dp[s_idx][t_idx]
        
        return res