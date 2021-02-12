"""
Given a string s and two letters l1 and l2, determine the minimum distance between occurences of these letters.
For example, if the string s is:
cfecf452d35ce2334f1c195d61691037dee93e8b210f45cfdc5acb94543c2cf31fa30b5f32fbf721
and the letters are 'a' and 'd',
output: 3

Explanation:
The string s contains the sequence 'dc5a', where the two characters are 3 positions apart.

"""

from collections import deque
import math
def closest(s, l1, l2):  # O(n) both 
    """
    DFS approach
    Go through the string and collect into a deque tuples (key, 1) where key is the index of letter l1
    Also mark as visited in the list visited
    start popping elements.
    Need to look at the neighbor from the left and the neighbor from the right.
    To avoid falling out of bounds, need to do it in two separate if statements. 
    Inside each statement we'll check if there is a match. If there is a match, it's enough.
    Otherwise keep going out and mark visited elements in visited.
    Refill the queue 
    """
    d = deque()
    res = 1
    visited = [False] * len(s)
    for key, value in enumerate(s):
        if value == l1:
            d.append((key, 1))
            visited[key] = True
    while d:
        curr_ix, curr_dist = d.popleft()
        if 0 < curr_ix:
            left_ch = s[curr_ix - 1]
            if not visited[curr_ix - 1]:
                if s[curr_ix - 1] == l2:
                    res = max(res, curr_dist)
                    break
                curr_dist += 1
                visited[curr_ix] = True
                d.append((curr_ix - 1, curr_dist))
        
        if curr_ix < len(s) - 1: 
            right_ch = s[curr_ix + 1]
            if not visited[curr_ix + 1]:
                if s[curr_ix + 1] == l2:
                    res = max(res, curr_dist)
                    break
                curr_dist += 1
                visited[curr_ix] = True
                d.append((curr_ix + 1, curr_dist))
    return res


def closest_brute_force(s, l1, l2):  # O(n^2) and O(n)
    """
    Collect indices into two lists and iterate in a double loop looking for the smallest abs difference 
    """
    l1_indices, l2_indices = [], []
    for k, v in enumerate(s):
        if v == l1:
            l1_indices.append(k)
        if v == l2:
            l2_indices.append(k)
    res = math.inf
    for num1 in l1_indices:
        for num2 in l2_indices:
            res = min(res, abs(num1 - num2))
    return res


if __name__ == '__main__':
    print(closest('cfecf452d35ce2334f1c195d61691037dee93e8b210f45cfdc5acb94543c2cf31fa30b5f32fbf721', 'a', 'd'))
    print(closest_brute_force('cfecf452d35ce2334f1c195d61691037dee93e8b210f45cfdc5acb94543c2cf31fa30b5f32fbf721', 'a', 'd'))
