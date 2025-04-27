"""
Consider an undirected tree with n vertices (1 to n). We start from vertex 1, and start walking on the tree via steps. The rules for each step:

Previously visited vertices can not be visited again.
When multiple vertices are possible, each of them are equally likely.
If there are no possible vertices to move to, we are forced to take a dummy step from the current vertex to the current vertex.
What is the probability that we are at vertex k after s steps?

Input: edges: List[List[int, int]], k int, s int
Output: prob float
"""

import collections
from typing import List

def prob_at_k(n: int, edges: List[List[int]], s: int, k: int) -> float:
    """
    Time: O(n) – each edge is traversed at most twice; and your recursion depth is at most the height of the tree (≤ n).
    Space: O(n) – for the adjacency list and the recursion stack.

    simple DFS (or BFS) from 1, keeping track of:

    your current time t
    the probability p you’ve accumulated so far
    the parent you came from (so you don’t go back)

    At each node u and time t:
    If t == s:
    if u == k you’ve found a valid “walk” and you add its probability to the answer;
    otherwise it contributes 0

    Otherwise (t < s):
    let c = the list of neighbors of u excluding its parent
    if c is empty, you’re forced to “stay” at u for all remaining steps; so if u == k you add p to the answer, otherwise 0
    else you spread your probability equally among the |c| children, and recurse on each with time t+1 and prob p/|c|

    We never revisit a node because we exclude the parent on each DFS call.
    When you reach time s, you only “count” paths that land you exactly at k.
    If you reach a dead‐end before time s, you’re forced to waste all remaining steps “staying” in place; hence you check again whether that place is k.
    """
    # build adjacency list
    g = collections.defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    ans = 0.0

    def dfs(u: int, parent: int, t: int, p: float):
        nonlocal ans
        # if we've taken s steps
        if t == s:
            if u == k:
                ans += p
            return

        # find unvisited neighbors
        children = [v for v in g[u] if v != parent]
        # if no place to go, we stay here for all remaining steps
        if not children:
            if u == k:
                ans += p
            return
        # otherwise, move to each child with equal probability
        share = p / len(children)
        for v in children:
            dfs(v, u, t + 1, share)

    # start at node 1, time 0, probability 1
    dfs(1, 0, 0, 1.0)
    return ans
