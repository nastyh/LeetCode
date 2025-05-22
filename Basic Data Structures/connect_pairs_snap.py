"""
Similar to https://leetcode.com/problems/valid-arrangement-of-pairs/description/


Connect Pairs 
Input : [Ba, _a, cb, dc]
output : _abcd

Input : [El, ll, lo, _h, he]
output : _hello

condition : the resultant string should begin with _

In this question, one had to connect the pairs. In this [Ba, _a, cb, dc] one example of pair is ba, _a, cb & dc.

Have to place pairs in a way such that second character in each pair is same as first character in next pair. Like :
[Ba, _a, cb, dc] to[ _a, ab, bc, cd]

Finally, remove all the redudant adjacent character : From [ _a, ab, bc, cd] to _abcd
"""
from collections import defaultdict
def connect_pairs(pairs):
    """
    O(n), n is the number of pairs for building the map and walking the path
    O(n), linear in the number of input pairs

    Build a graph from the list of 2-character strings: each string like "ab" represents a directed edge from 'a' to 'b'.
    start_map: from each pair's first character to the pair itself. This helps us chain the next pair based on the current one’s second character
    in_degree: to find the starting point — the only character with in-degree 0.
    Find the starting pair: the one starting with '_'.
    Traverse using the mapping: follow from one pair to the next using start_map[current[1]
    Build the result: start with the first pair, and for all following pairs, append only the second character to avoid redundancy
    """
    # Map from starting character to the full string
    start_map = {}
    in_degree = defaultdict(int)

    for pair in pairs:
        start, end = pair[0], pair[1]
        start_map[start] = pair
        in_degree[end] += 1

    # Find the starting point — the one with '_'
    current = None
    for pair in pairs:
        if pair[0] == '_':
            current = pair
            break

    if not current:
        return ""  # No valid starting point

    result = current  # Start with the whole pair
    while current[1] in start_map:
        next_pair = start_map[current[1]]
        result += next_pair[1]  # Append only the new character
        current = next_pair

    return result

# Test cases
print(connect_pairs(["Ba", "_a", "cb", "dc"]))  # Output: _abcd
print(connect_pairs(["El", "ll", "lo", "_h", "he"]))  # Output: _hello
