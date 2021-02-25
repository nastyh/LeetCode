from collections import deque, defaultdict
"""
Given a set of tasks, the dependencies between them and the time that it takes to complete each one.
1) Find the minimum amount of time that it takes to complete a particular task given 
the constraint that at most 1 task can be worked on at a given time 
(if its prerequisites are complete).
Input: 

Task: A, Dependencies: B, C Time To Complete A: 5 
Task: B, Dependencies: D    Time To Complete B: 4
Task: C, Dependencies:      Time To Complete C: 2
Task: D, Dependencies:      Time to Complete D: 2
Output: 
Total Time to Complete A: 13 
Input: 
Task: A, Dependencies: B, C Time To Complete A: 5
Task: B, Dependencies: D    Time To Complete B: 4
Task: C, Dependencies:      Time To Complete C: 2
Task: D, Dependencies:      Time to Complete D: 2
Task: E, Dependencies:      Time to Complete E: 5

Output: 
Total Time to Complete A: 13
Total Time to Complete E: 5

[[A, [B,C], 5], [B, [D], 4], [C, [], 2], [D, [], 2]]
"""

def time_to_finish_dfs(nums):  # Probably doesn't pass edge cases
    adj_list, times, res = {}, {}, 0
    for element in nums:
        adj_list[element[0]] = element[1]
        times[element[0]] = element[2]
        # depth[element[0]] = len(element[1])
    # print(times)
    visited = set()
    def _helper(candidate, times, adj_list):
        nonlocal res
        nonlocal visited
        if len(adj_list[candidate]) == 0:
            res += times[candidate]
        for neighbor in adj_list[candidate]:
            # print(neighbor)
            for element in neighbor:
                if element not in visited:
                    visited.add(element)
                    _helper(element, times, adj_list)
    for task in adj_list.keys():
        _helper(task, times, adj_list)
    return res


if __name__ == '__main__': 
    # print(time_to_finish([['A', ['B','C'], 5], ['B', ['D'], 4], ['C', [], 2], ['D', [], 2]]))
    print(time_to_finish_dfs([['A', ['B','C'], 5], ['B', ['D'], 4], ['C', [], 2], ['D', [], 2]]))
    # print(time_to_finish_dfs([['C', [], 2], ['D', [], 2]]))
    print(time_to_finish_dfs([['A', ['B','C'], 5], ['B', ['D'], 4], ['C', [], 2], ['D', [], 2], ['E', [], 5]]))