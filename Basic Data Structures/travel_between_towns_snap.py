"""
https://leetcode.com/discuss/post/3664499/snap-phone-mle-2-by-anonymous_user-yv9y/
like 332 https://leetcode.com/problems/reconstruct-itinerary/description/

here are multiple towns within one City. And sometimes people may travel through different towns
Suppose you are given the start towns and end towns for each trip, and there might be many trips
Can you find all valid trips?
You can only use one trip only one time, must use all trips
You can assume there are at least one valid solution

Let's assume you will always start from 'A'

Example 1
Input: [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
Assum you will always start with 'A'
Meaning: A ==> B, B ==> C, C ==> D, D ==> E
Output: [A, B, C, D, E]

Example 2
Input: [['A', 'B'], ['B', 'C'], ['C', 'B'], ['B', 'A'],["A","C]]
A ==> B, B ==> C, C ==> B, B ==> A, A ==> C
Output_1: A, B, C, B, A, C
Output_2: A, C, B, A, B, C
Output_3: A, C, B, A, B, C
final output should be [[ A, B, C, B, A, C],[A, C, B, A, B, C],[A, C, B, A, B, C]]
"""
from collections import defaultdict, deque
from typing import Counter

def find_all_paths_bfs(trips):
    """
    O(n! * n)
    O(n! * n), stores all intermediate states

    current_path: list of nodes visited so far (e.g., ['A', 'B'])
    used_edges: multiset (like Counter) of remaining trips to use
    Take the current town (last in current_path)

    Look for all remaining trips starting from this town
    For each, create a new state:
    Extend current_path
    Mark trip as used (decrement from Counter)
    Add to queue
    """
    d = defaultdict(list)
    edges = Counter()
    n = len(trips)
    res = []

    for start, end in trips:
        d[start].append(end) # town: [list where you can go from here]
        edges[(start, end)] += 1
    
    d = deque()
    d.append((['A'], edges.copy()))

    while d:
        path, remaining = d.popleft()

        if sum(remaining.values()) == 0:
            res.append(path)
            continue

        last = path[-1]
        for neighbor in d[last]:
            if remaining[(last, neighbor)] > 0:
                new_remaining = remaining.copy()
                new_remaining[(last, neighbor)] -= 1
                d.append((path + [neighbor], new_remaining))

    return res


def find_all_paths_dfs(trips):
    """
    O(n! * n) n is len(trips)
    the number of valid permutations of n edges (trips) where each is used exactly once can be up to O(n!).
    Each path takes O(n) time to construct (we copy the path when we reach a full solution).

    O(kn), k is the num of valid paths
    d and edges are O(n) each
    call stack is the same 
    result list: O(kn)

    backtracking to explore all valid paths.
    edges ensures each trip is used exactly once.
    """
    d = defaultdict(list)
    edges = Counter()
    res, total_edges = [], len(trips)

    for start, end in trips:
        d[start].append(end) # town: [list where you can go from here]
        edges[(start, end)] += 1
    
    def dfs(node, path):
        if len(path) == total_edges + 1:
            res.append(path[:])
            return

        for neighbor in list(d[node]):
            if edges[(node, neighbor)] > 0:
                edges[(node, neighbor)] -= 1
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
                edges[(node, neighbor)] += 1
    dfs('A', ['A'])
    return res


